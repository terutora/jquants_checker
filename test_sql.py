import json
import requests
import os
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
    LocalCode VARCHAR(255),
    DisclosureNumber VARCHAR(255) UNIQUE,
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
    NonConsolidatedBookValuePerShare VARCHAR(255)
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


exclude_list = ['''
DisclosedTime,
NumberOfIssuedAndOutstandingSharesAtTheEndOfFiscalYearIncludingTreasuryStock,
NextYearForecastDistributionsPerUnit(REIT),
DistributionsPerUnit(REIT),
ForecastDistributionsPerUnit(REIT)
ForecastNonConsolidatedNetSales2ndQuarter,
ForecastNonConsolidatedOperatingProfit2ndQuarter,
ForecastNonConsolidatedOrdinaryProfit2ndQuarter,
ForecastNonConsolidatedProfit2ndQuarter,
ForecastNonConsolidatedEarningsPerShare2ndQuarter,
NextYearForecastNonConsolidatedNetSales2ndQuarter,
NextYearForecastNonConsolidatedOperatingProfit2ndQuarter,
NextYearForecastNonConsolidatedOrdinaryProfit2ndQuarter,
NextYearForecastNonConsolidatedProfit2ndQuarter,
NextYearForecastNonConsolidatedEarningsPerShare2ndQuarter,
ForecastNonConsolidatedNetSales,
ForecastNonConsolidatedOperatingProfit,
ForecastNonConsolidatedOrdinaryProfit,
ForecastNonConsolidatedProfit,
ForecastNonConsolidatedEarningsPerShare,
NextYearForecastNonConsolidatedNetSales,
NextYearForecastNonConsolidatedOperatingProfit,
NextYearForecastNonConsolidatedOrdinaryProfit,
NextYearForecastNonConsolidatedProfit,
NextYearForecastNonConsolidatedEarningsPerShare
''']

a = requests.get(f"https://api.jquants.com/v1/fins/statements?code={1301}", headers=headers)
st = a.json()
f_list = st["statements"]


# 特定のキーを除外して新たに辞書を作成

fin_list = [{k: v for k, v in d.items() if k not in [exclude_list]} for d in f_list]
print(f_list)
# リストのデータをテーブルに挿入
for item in fin_list:
    columns = ', '.join(item.keys())
    placeholders = ', '.join(['%s'] * len(item))
    insert_query = f"INSERT INTO code_db ({columns}) VALUES ({placeholders}) ON DUPLICATE KEY UPDATE DisclosureNumber=DisclosureNumber"
    cursor.execute(insert_query, tuple(item.values()))

# コミットして変更を保存
conn.commit()