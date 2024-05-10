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
    'database': 'info_db'
}

conn = mysql.connector.connect(**config)
cursor = conn.cursor()

# テーブル作成のクエリ
create_table_query = """
CREATE TABLE IF NOT EXISTS code_db (
    DisclosedDate TEXT,
    DisclosedTime TEXT,
    LocalCode TEXT,
    DisclosureNumber TEXT,
    TypeOfDocument TEXT,
    TypeOfCurrentPeriod TEXT,
    CurrentPeriodStartDate TEXT,
    CurrentPeriodEndDate TEXT,
    CurrentFiscalYearStartDate TEXT,
    CurrentFiscalYearEndDate TEXT,
    NextFiscalYearStartDate TEXT,
    NextFiscalYearEndDate TEXT,
    NetSales TEXT,
    OperatingProfit TEXT,
    OrdinaryProfit TEXT,
    Profit TEXT,
    EarningsPerShare TEXT,
    DilutedEarningsPerShare TEXT,
    TotalAssets TEXT,
    Equity TEXT,
    EquityToAssetRatio TEXT,
    BookValuePerShare TEXT,
    CashFlowsFromOperatingActivities TEXT,
    CashFlowsFromInvestingActivities TEXT,
    CashFlowsFromFinancingActivities TEXT,
    CashAndEquivalents TEXT,
    ResultDividendPerShare1stQuarter TEXT,
    ResultDividendPerShare2ndQuarter TEXT,
    ResultDividendPerShare3rdQuarter TEXT,
    ResultDividendPerShareFiscalYearEnd TEXT,
    ResultDividendPerShareAnnual TEXT,
    ResultTotalDividendPaidAnnual TEXT,
    ResultPayoutRatioAnnual TEXT,
    ForecastDividendPerShare1stQuarter TEXT,
    ForecastDividendPerShare2ndQuarter TEXT,
    ForecastDividendPerShare3rdQuarter TEXT,
    ForecastDividendPerShareFiscalYearEnd TEXT,
    ForecastDividendPerShareAnnual TEXT,
    ForecastTotalDividendPaidAnnual TEXT,
    ForecastPayoutRatioAnnual TEXT,
    NextYearForecastDividendPerShare1stQuarter TEXT,
    NextYearForecastDividendPerShare2ndQuarter TEXT,
    NextYearForecastDividendPerShare3rdQuarter TEXT,
    NextYearForecastDividendPerShareFiscalYearEnd TEXT,
    NextYearForecastDividendPerShareAnnual TEXT,
    NextYearForecastPayoutRatioAnnual TEXT,
    ForecastNetSales2ndQuarter TEXT,
    ForecastOperatingProfit2ndQuarter TEXT,
    ForecastOrdinaryProfit2ndQuarter TEXT,
    ForecastProfit2ndQuarter TEXT,
    ForecastEarningsPerShare2ndQuarter TEXT,
    NextYearForecastNetSales2ndQuarter TEXT,
    NextYearForecastOperatingProfit2ndQuarter TEXT,
    NextYearForecastOrdinaryProfit2ndQuarter TEXT,
    NextYearForecastProfit2ndQuarter TEXT,
    NextYearForecastEarningsPerShare2ndQuarter TEXT,
    ForecastNetSales TEXT,
    ForecastOperatingProfit TEXT,
    ForecastOrdinaryProfit TEXT,
    ForecastProfit TEXT,
    ForecastEarningsPerShare TEXT,
    NextYearForecastNetSales TEXT,
    NextYearForecastOperatingProfit TEXT,
    NextYearForecastOrdinaryProfit TEXT,
    NextYearForecastProfit TEXT,
    NextYearForecastEarningsPerShare TEXT,
    MaterialChangesInSubsidiaries TEXT,
    ChangesBasedOnRevisionsOfAccountingStandard TEXT,
    ChangesOtherThanOnesBasedOnRevisionsOfAccountingStandard TEXT,
    ChangesInAccountingEstimates TEXT,
    RetrospectiveRestatement TEXT,
    NumberOfTreasuryStockAtTheEndOfFiscalYear TEXT,
    AverageNumberOfShares TEXT,
    NonConsolidatedNetSales TEXT,
    NonConsolidatedOperatingProfit TEXT,
    NonConsolidatedOrdinaryProfit TEXT,
    NonConsolidatedProfit TEXT,
    NonConsolidatedEarningsPerShare TEXT,
    NonConsolidatedTotalAssets TEXT,
    NonConsolidatedEquity TEXT,
    NonConsolidatedEquityToAssetRatio TEXT,
    NonConsolidatedBookValuePerShare TEXT,
    ForecastNonConsolidatedNetSales2ndQuarter TEXT,
    ForecastNonConsolidatedOperatingProfit2ndQuarter TEXT,
    ForecastNonConsolidatedOrdinaryProfit2ndQuarter TEXT,
    ForecastNonConsolidatedProfit2ndQuarter TEXT,
    ForecastNonConsolidatedEarningsPerShare2ndQuarter TEXT,
    NextYearForecastNonConsolidatedNetSales2ndQuarter TEXT,
    NextYearForecastNonConsolidatedOperatingProfit2ndQuarter TEXT,
    NextYearForecastNonConsolidatedOrdinaryProfit2ndQuarter TEXT,
    NextYearForecastNonConsolidatedProfit2ndQuarter TEXT,
    NextYearForecastNonConsolidatedEarningsPerShare2ndQuarter TEXT,
    ForecastNonConsolidatedNetSales TEXT,
    ForecastNonConsolidatedOperatingProfit TEXT,
    ForecastNonConsolidatedOrdinaryProfit TEXT,
    ForecastNonConsolidatedProfit TEXT,
    ForecastNonConsolidatedEarningsPerShare TEXT,
    NextYearForecastNonConsolidatedNetSales TEXT,
    NextYearForecastNonConsolidatedOperatingProfit TEXT,
    NextYearForecastNonConsolidatedOrdinaryProfit TEXT,
    NextYearForecastNonConsolidatedProfit TEXT,
    NextYearForecastNonConsolidatedEarningsPerShare TEXT
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
f_list = st["statements"]

# 除外するキーを含む辞書を除外する

fin_list = [d for d in f_list if 'NumberOfIssuedAndOutstandingSharesAtTheEndOfFiscalYearIncludingTreasuryStock' not in d or 'DistributionsPerUnit(REIT)' not in d or 'ForecastDistributionsPerUnit(REIT)' not in d or 'NextYearForecastDistributionsPerUnit(REIT)' not in d]

# リストのデータをテーブルに挿入
for item in fin_list:
    columns = ', '.join(item.keys())
    placeholders = ', '.join(['%s'] * len(item))
    insert_query = f"INSERT INTO code_info ({columns}) VALUES ({placeholders})"
    cursor.execute(insert_query, tuple(item.values()))

# コミットして変更を保存
conn.commit()
