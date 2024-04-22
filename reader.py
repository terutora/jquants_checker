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

exclude_key = 'MarketCodeName'  # 除外するキー
exclude_value = 'その他'    # 除外する値

# 特定のキーと値を含む辞書を除外する
filtered_list = [d for d in tick_list if exclude_key not in d or d[exclude_key] != exclude_value]

codes = [d["Code"] for d in filtered_list]
new_list = [int(str(num)[:-1]) for num in codes]

# Excelファイルを読み込む
excel_file = 'out_st.xlsx'
for i_code in new_list:
    df = pd.read_excel(excel_file, sheet_name=f'{i_code}')

    # HTML形式で出力する
    html_output = df.to_html()

    # HTMLファイルに書き出す
    with open('output.html', 'w') as f:
        f.write(html_output)
