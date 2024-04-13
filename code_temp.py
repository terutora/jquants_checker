import json
import pandas as pd
import requests
import os

# 特定の環境変数を取得
MY_EMAIL = os.environ.get('my_email')
PASS = os.environ.get('password')

# リフレッシュトークンを取得
resp = requests.post(
    "https://api.jquants.com/v1/token/auth_user",
    data=json.dumps({"mailaddress": MY_EMAIL, "password": PASS})
)
REFRESH_TOKEN = resp.json()["refreshToken"]

# IDトークンを取得
resp = requests.post(
    "https://api.jquants.com/v1/token/auth_refresh",
    params={"refreshtoken": REFRESH_TOKEN}
)

ID_TOKEN = resp.json()["idToken"]

headers = {'Authorization': 'Bearer {}'.format(ID_TOKEN)}
r = requests.get("https://api.jquants.com/v1/listed/info", headers=headers)
list = r.json()
tick_list = list["info"]
codes = [d["Code"] for d in tick_list]
new_list = [int(str(num)[:-1]) for num in codes]
#print(new_list)

from openpyxl import Workbook

new_list = [1305,9997]

for i_code in new_list:
    a = requests.get(f"https://api.jquants.com/v1/fins/statements?code={i_code}", headers=headers)
    st = a.json()
    fin_list = st["statements"]

    # 既存のExcelファイルを読み込む
    existing_file = "out_st.xlsx"
    writer = pd.ExcelWriter(existing_file, engine='openpyxl', mode='a')

    # リストをDataFrameに変換
    df = pd.DataFrame(fin_list)

    # データを既存のExcelファイルに書き込む（シート名を指定して）
    df.to_excel(writer, sheet_name=f"{i_code}", index=False)

    # ファイルを保存してExcelWriterを閉じる
    writer._save()
    writer.close()
