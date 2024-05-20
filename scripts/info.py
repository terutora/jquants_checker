import json
import requests
import os
import mysql.connector
from dotenv import load_dotenv

# .envファイルを読み込む
load_dotenv()

print("DB_HOST:", os.getenv('DB_HOST'))
print("DB_USER:", os.getenv('DB_USER'))
print("DB_PASSWORD:", os.getenv('DB_PASSWORD'))
print("DB_NAME:", os.getenv('DB_NAME'))

# リフレッシュトークンを取得
resp = requests.post(
    "https://api.jquants.com/v1/token/auth_user",
    data=json.dumps({"mailaddress": os.getenv('API_KEY_MY_EMAIL'), "password": os.getenv('API_KEY_MY_PASSWORD')})
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
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'host': os.getenv('DB_HOST'),
    'database': os.getenv('DB_NAME'),
    'charset': 'utf8mb4'
}

# MySQLに接続
conn = mysql.connector.connect(**config)
cursor = conn.cursor()

# テーブル作成のクエリ
create_table_query = """
CREATE TABLE IF NOT EXISTS basic_info (
    Date VARCHAR(255),
    Code VARCHAR(255) UNIQUE,
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
    # データが既に存在するか確認
    cursor.execute("SELECT COUNT(*) FROM basic_info WHERE Code = %s", (item['Code'],))
    count = cursor.fetchone()[0]
    
    if count == 0:
        # データが存在しない場合のみ挿入
        columns = ', '.join(item.keys())
        placeholders = ', '.join(['%s'] * len(item))
        insert_query = f"INSERT INTO basic_info ({columns}) VALUES ({placeholders})"
        cursor.execute(insert_query, tuple(item.values()))
# コミットして変更を保存
conn.commit()