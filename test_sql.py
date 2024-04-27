import json
import pandas as pd
import requests
import os
from openpyxl import Workbook
import mysql.connector

# 特定の環境変数を取得
MY_EMAIL = os.environ.get('my_email')
PASS = os.environ.get('password')
PASSWORD = os.environ.get('pass')

config = {
    'host': 'localhost',
    'user': 'root',
    "password": PASSWORD,
    'database': 'finance_db'
}

conn = mysql.connector.connect(**config)
cursor = conn.cursor()

create_table_query = """
CREATE TABLE IF NOT EXISTS stock_codes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    code INT,
    name VARCHAR(255),
    market_code VARCHAR(255)
)
"""
cursor.execute(create_table_query)


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
'''
for i_code in codes:
    a = requests.get(f"https://api.jquants.com/v1/fins/statements?code={i_code}", headers=headers)
    st = a.json()
    fin_list = st["statements"]
'''
a = requests.get(f"https://api.jquants.com/v1/fins/statements?code={1301}", headers=headers)
st = a.json()
fin_list = st["statements"]

for item in fin_list:
    # データを挿入するクエリを動的に生成する
    insert_query = f"INSERT INTO stock_codes ({', '.join(item.keys())}) VALUES ({', '.join(['%s' for _ in item])})"
    
    # データを挿入する
    cursor.execute(insert_query, tuple(item.values()))



# コミットして変更を保存
conn.commit()

# 接続を閉じる
cursor.close()
conn.close()