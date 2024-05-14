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
    DisclosedDate VARCHAR(100),
    LocalCode VARCHAR(100),
    DisclosureNumber VARCHAR(100) UNIQUE,
    TypeOfDocument VARCHAR(100),
    TypeOfCurrentPeriod VARCHAR(100),
    CurrentPeriodStartDate VARCHAR(100),
    CurrentPeriodEndDate VARCHAR(100),
    CurrentFiscalYearStartDate VARCHAR(100),
    CurrentFiscalYearEndDate VARCHAR(100),
    NextFiscalYearStartDate VARCHAR(100),
    NextFiscalYearEndDate VARCHAR(100),
    NetSales VARCHAR(100),
    OperatingProfit VARCHAR(100),
    OrdinaryProfit VARCHAR(100),
    Profit VARCHAR(100),
    EarningsPerShare VARCHAR(100),
    DilutedEarningsPerShare VARCHAR(100),
    TotalAssets VARCHAR(100),
    Equity VARCHAR(100),
    EquityToAssetRatio VARCHAR(100),
    BookValuePerShare VARCHAR(100),
    CashFlowsFromOperatingActivities VARCHAR(100),
    CashFlowsFromInvestingActivities VARCHAR(100),
    CashFlowsFromFinancingActivities VARCHAR(100),
    CashAndEquivalents VARCHAR(100),
    ResultDividendPerShare1stQuarter VARCHAR(100),
    ResultDividendPerShare2ndQuarter VARCHAR(100),
    ResultDividendPerShare3rdQuarter VARCHAR(100),
    ResultDividendPerShareFiscalYearEnd VARCHAR(100),
    ResultDividendPerShareAnnual VARCHAR(100),
    ResultTotalDividendPaidAnnual VARCHAR(100),
    ResultPayoutRatioAnnual VARCHAR(100),
    ForecastDividendPerShare1stQuarter VARCHAR(100),
    ForecastDividendPerShare2ndQuarter VARCHAR(100),
    ForecastDividendPerShare3rdQuarter VARCHAR(100),
    ForecastDividendPerShareFiscalYearEnd VARCHAR(100),
    ForecastDividendPerShareAnnual VARCHAR(100),
    ForecastTotalDividendPaidAnnual VARCHAR(100),
    ForecastPayoutRatioAnnual VARCHAR(100),
    NextYearForecastDividendPerShare1stQuarter VARCHAR(100),
    NextYearForecastDividendPerShare2ndQuarter VARCHAR(100),
    NextYearForecastDividendPerShare3rdQuarter VARCHAR(100),
    NextYearForecastDividendPerShareFiscalYearEnd VARCHAR(100),
    NextYearForecastDividendPerShareAnnual VARCHAR(100),
    NextYearForecastPayoutRatioAnnual VARCHAR(100),
    ForecastNetSales2ndQuarter VARCHAR(100),
    ForecastOperatingProfit2ndQuarter VARCHAR(100),
    ForecastOrdinaryProfit2ndQuarter VARCHAR(100),
    ForecastProfit2ndQuarter VARCHAR(100),
    ForecastEarningsPerShare2ndQuarter VARCHAR(100),
    NextYearForecastNetSales2ndQuarter VARCHAR(100),
    NextYearForecastOperatingProfit2ndQuarter VARCHAR(100),
    NextYearForecastOrdinaryProfit2ndQuarter VARCHAR(100),
    NextYearForecastProfit2ndQuarter VARCHAR(100),
    NextYearForecastEarningsPerShare2ndQuarter VARCHAR(100),
    ForecastNetSales VARCHAR(100),
    ForecastOperatingProfit VARCHAR(100),
    ForecastOrdinaryProfit VARCHAR(100),
    ForecastProfit VARCHAR(100),
    ForecastEarningsPerShare VARCHAR(100),
    NextYearForecastNetSales VARCHAR(100),
    NextYearForecastOperatingProfit VARCHAR(100),
    NextYearForecastOrdinaryProfit VARCHAR(100),
    NextYearForecastProfit VARCHAR(100),
    NextYearForecastEarningsPerShare VARCHAR(100),
    MaterialChangesInSubsidiaries VARCHAR(100),
    ChangesBasedOnRevisionsOfAccountingStandard VARCHAR(100),
    ChangesOtherThanOnesBasedOnRevisionsOfAccountingStandard VARCHAR(100),
    ChangesInAccountingEstimates VARCHAR(100),
    RetrospectiveRestatement VARCHAR(100),
    NumberOfTreasuryStockAtTheEndOfFiscalYear VARCHAR(100),
    AverageNumberOfShares VARCHAR(100),
    NonConsolidatedNetSales VARCHAR(100),
    NonConsolidatedOperatingProfit VARCHAR(100),
    NonConsolidatedOrdinaryProfit VARCHAR(100),
    NonConsolidatedProfit VARCHAR(100),
    NonConsolidatedEarningsPerShare VARCHAR(100),
    NonConsolidatedTotalAssets VARCHAR(100),
    NonConsolidatedEquity VARCHAR(100),
    NonConsolidatedEquityToAssetRatio VARCHAR(100),
    NonConsolidatedBookValuePerShare VARCHAR(100)
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

# 特定のキーを除外する関数
def exclude_keys(d, exclude_list):
    return {key: value for key, value in d.items() if key not in exclude_list}

exclude_list = [
    'DisclosedTime',
    'NumberOfIssuedAndOutstandingSharesAtTheEndOfFiscalYearIncludingTreasuryStock',
    'NextYearForecastDistributionsPerUnit(REIT)',
    'DistributionsPerUnit(REIT)',
    'ForecastDistributionsPerUnit(REIT)',
    'ForecastNonConsolidatedNetSales2ndQuarter',
    'ForecastNonConsolidatedOperatingProfit2ndQuarter',
    'ForecastNonConsolidatedOrdinaryProfit2ndQuarter',
    'ForecastNonConsolidatedProfit2ndQuarter',
    'ForecastNonConsolidatedEarningsPerShare2ndQuarter',
    'NextYearForecastNonConsolidatedNetSales2ndQuarter',
    'NextYearForecastNonConsolidatedOperatingProfit2ndQuarter',
    'NextYearForecastNonConsolidatedOrdinaryProfit2ndQuarter',
    'NextYearForecastNonConsolidatedProfit2ndQuarter',
    'NextYearForecastNonConsolidatedEarningsPerShare2ndQuarter',
    'ForecastNonConsolidatedNetSales',
    'ForecastNonConsolidatedOperatingProfit',
    'ForecastNonConsolidatedOrdinaryProfit',
    'ForecastNonConsolidatedProfit',
    'ForecastNonConsolidatedEarningsPerShare',
    'NextYearForecastNonConsolidatedNetSales',
    'NextYearForecastNonConsolidatedOperatingProfit',
    'NextYearForecastNonConsolidatedOrdinaryProfit',
    'NextYearForecastNonConsolidatedProfit',
    'NextYearForecastNonConsolidatedEarningsPerShare'
]

r = requests.get("https://api.jquants.com/v1/listed/info", headers=headers)
list = r.json()
tick_list = list["info"]

exclude_key = 'MarketCodeName'  # 除外するキー
exclude_value = 'その他'    # 除外する値

# 特定のキーと値を含む辞書を除外する
filtered_list = [d for d in tick_list if exclude_key not in d or d[exclude_key] != exclude_value]

codes = [d["Code"] for d in filtered_list]

for i_code in codes:
    api = requests.get(f"https://api.jquants.com/v1/fins/statements?code={i_code}", headers=headers)
    st = api.json()
    f_list = st["statements"]

    # 特定のキーを除外して新たに辞書を作成
    fin_list = [exclude_keys(d, exclude_list) for d in f_list]

    # リストのデータをテーブルに挿入
    for item in fin_list:
        columns = ', '.join(item.keys())
        placeholders = ', '.join(['%s'] * len(item))
        insert_query = f"INSERT INTO code_db ({columns}) VALUES ({placeholders}) ON DUPLICATE KEY UPDATE {', '.join([f'{k} = VALUES({k})' for k in item.keys()])}"
        cursor.execute(insert_query, tuple(item.values()))

    # コミットして変更を保存
    conn.commit()