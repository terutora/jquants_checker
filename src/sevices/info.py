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

config = {
    'host': 'localhost',
    'user': 'root',
    "password": PASSWORD,
    'database': 'info_db'
}

# MySQLに接続
conn = mysql.connector.connect(**config)
cursor = conn.cursor()

# テーブル作成のクエリ
create_table_query = """
CREATE TABLE IF NOT EXISTS my_table (
    Date VARCHAR(255),
    Code VARCHAR(255),
    CompanyName VARCHAR(255),
    CompanyNameEnglish VARCHAR(255),
    Sector17Code VARCHAR(255),
    Sector17CodeName VARCHAR(255),
    Sector33Code VARCHAR(255),
    Sector33CodeName VARCHAR(255),
    ScaleCategory VARCHAR(255),
    MarketCode VARCHAR(255),
    MarketCodeName VARCHAR(255)
    )
"""
cursor.execute(create_table_query)

# リストのデータをテーブルに挿入
for item in tick_list:
    columns = ', '.join(item.keys())
    placeholders = ', '.join(['%s'] * len(item))
    insert_query = f"INSERT INTO besic_info ({columns}) VALUES ({placeholders})"
    cursor.execute(insert_query, tuple(item.values()))

# コミットして変更を保存
conn.commit()