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
    DisclosedDate VARCHAR(255),
    DisclosedTime VARCHAR(255),
    LocalCode VARCHAR(255),
    DisclosureNumber VARCHAR(255),
    TypeOfDocument VARCHAR(255),
    TypeOfCurrentPeriod VARCHAR(255),
    CurrentPeriodStartDate VARCHAR(255),
    CurrentPeriodEndDate VARCHAR(255),
    CurrentFiscalYearStartDate VARCHAR(255),
    CurrentFiscalYearEndDate VARCHAR(255),
    NextFiscalYearStartDate VARCHAR(255),
    NextFiscalYearEndDate VARCHAR(255),
    NetSales VARCHAR(255),
    OperatingProfit VARCHAR(255),
    OrdinaryProfit VARCHAR(255),
    Profit VARCHAR(255),
    EarningsPerShare VARCHAR(255),
    DilutedEarningsPerShare VARCHAR(255),
    TotalAssets VARCHAR(255),
    Equity VARCHAR(255),
    EquityToAssetRatio VARCHAR(255),
    BookValuePerShare VARCHAR(255),
    CashFlowsFromOperatingActivities VARCHAR(255),
    CashFlowsFromInvestingActivities VARCHAR(255),
    CashFlowsFromFinancingActivities VARCHAR(255),
    CashAndEquivalents VARCHAR(255),
    ResultDividendPerShare1stQuarter VARCHAR(255),
    ResultDividendPerShare2ndQuarter VARCHAR(255),
    ResultDividendPerShare3rdQuarter VARCHAR(255),
    ResultDividendPerShareFiscalYearEnd VARCHAR(255),
    ResultDividendPerShareAnnual VARCHAR(255),
    ResultTotalDividendPaidAnnual VARCHAR(255),
    ResultPayoutRatioAnnual VARCHAR(255),
    ForecastDividendPerShare1stQuarter VARCHAR(255),
    ForecastDividendPerShare2ndQuarter VARCHAR(255),
    ForecastDividendPerShare3rdQuarter VARCHAR(255),
    ForecastDividendPerShareFiscalYearEnd VARCHAR(255),
    ForecastDividendPerShareAnnual VARCHAR(255),
    ForecastTotalDividendPaidAnnual VARCHAR(255),
    ForecastPayoutRatioAnnual VARCHAR(255),
    NextYearForecastDividendPerShare1stQuarter VARCHAR(255),
    NextYearForecastDividendPerShare2ndQuarter VARCHAR(255),
    NextYearForecastDividendPerShare3rdQuarter VARCHAR(255),
    NextYearForecastDividendPerShareFiscalYearEnd VARCHAR(255),
    NextYearForecastDividendPerShareAnnual VARCHAR(255),
    NextYearForecastPayoutRatioAnnual VARCHAR(255),
    ForecastNetSales2ndQuarter VARCHAR(255),
    ForecastOperatingProfit2ndQuarter VARCHAR(255),
    ForecastOrdinaryProfit2ndQuarter VARCHAR(255),
    ForecastProfit2ndQuarter VARCHAR(255),
    ForecastEarningsPerShare2ndQuarter VARCHAR(255),
    NextYearForecastNetSales2ndQuarter VARCHAR(255),
    NextYearForecastOperatingProfit2ndQuarter VARCHAR(255),
    NextYearForecastOrdinaryProfit2ndQuarter VARCHAR(255),
    NextYearForecastProfit2ndQuarter VARCHAR(255),
    NextYearForecastEarningsPerShare2ndQuarter VARCHAR(255),
    ForecastNetSales VARCHAR(255),
    ForecastOperatingProfit VARCHAR(255),
    ForecastOrdinaryProfit VARCHAR(255),
    ForecastProfit VARCHAR(255),
    ForecastEarningsPerShare VARCHAR(255),
    NextYearForecastNetSales VARCHAR(255),
    NextYearForecastOperatingProfit VARCHAR(255),
    NextYearForecastOrdinaryProfit VARCHAR(255),
    NextYearForecastProfit VARCHAR(255),
    NextYearForecastEarningsPerShare VARCHAR(255),
    MaterialChangesInSubsidiaries VARCHAR(255),
    ChangesBasedOnRevisionsOfAccountingStandard VARCHAR(255),
    ChangesOtherThanOnesBasedOnRevisionsOfAccountingStandard VARCHAR(255),
    ChangesInAccountingEstimates VARCHAR(255),
    RetrospectiveRestatement VARCHAR(255),
    NumberOfTreasuryStockAtTheEndOfFiscalYear VARCHAR(255),
    AverageNumberOfShares VARCHAR(255),
    NonConsolidatedNetSales VARCHAR(255),
    NonConsolidatedOperatingProfit VARCHAR(255),
    NonConsolidatedOrdinaryProfit VARCHAR(255),
    NonConsolidatedProfit VARCHAR(255),
    NonConsolidatedEarningsPerShare VARCHAR(255),
    NonConsolidatedTotalAssets VARCHAR(255),
    NonConsolidatedEquity VARCHAR(255),
    NonConsolidatedEquityToAssetRatio VARCHAR(255),
    NonConsolidatedBookValuePerShare VARCHAR(255),
    ForecastNonConsolidatedNetSales2ndQuarter VARCHAR(255),
    ForecastNonConsolidatedOperatingProfit2ndQuarter VARCHAR(255),
    ForecastNonConsolidatedOrdinaryProfit2ndQuarter VARCHAR(255),
    ForecastNonConsolidatedProfit2ndQuarter VARCHAR(255),
    ForecastNonConsolidatedEarningsPerShare2ndQuarter VARCHAR(255),
    NextYearForecastNonConsolidatedNetSales2ndQuarter VARCHAR(255),
    NextYearForecastNonConsolidatedOperatingProfit2ndQuarter VARCHAR(255),
    NextYearForecastNonConsolidatedOrdinaryProfit2ndQuarter VARCHAR(255),
    NextYearForecastNonConsolidatedProfit2ndQuarter VARCHAR(255),
    NextYearForecastNonConsolidatedEarningsPerShare2ndQuarter VARCHAR(255),
    ForecastNonConsolidatedNetSales VARCHAR(255),
    ForecastNonConsolidatedOperatingProfit VARCHAR(255),
    ForecastNonConsolidatedOrdinaryProfit VARCHAR(255),
    ForecastNonConsolidatedProfit VARCHAR(255),
    ForecastNonConsolidatedEarningsPerShare VARCHAR(255),
    NextYearForecastNonConsolidatedNetSales VARCHAR(255),
    NextYearForecastNonConsolidatedOperatingProfit VARCHAR(255),
    NextYearForecastNonConsolidatedOrdinaryProfit VARCHAR(255),
    NextYearForecastNonConsolidatedProfit VARCHAR(255),
    NextYearForecastNonConsolidatedEarningsPerShare VARCHAR(255)
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
