<template>
<div>
    <h1>データハンドラ</h1>
    <p>データを処理しています...</p>
</div>
</template>

<script>

export default {
    name: 'DataHandler',
    created() {
        const data = JSON.parse(this.$route.query.data);
        const keysToFilter = [
        'DisclosedDate',
        'TypeOfDocument',
        'NetSales',
        'OperatingProfit',
        'OrdinaryProfit',
        'Profit',
        'EarningsPerShare',
        'TotalAssets',
        'Equity',
        'EquityToAssetRatio',
        'BookValuePerShare',
        'CashFlowsFromOperatingActivities',
        'CashFlowsFromInvestingActivities',
        'CashFlowsFromFinancingActivities',
        'CashAndEquivalents',
        'ResultDividendPerShareAnnual',
        'ResultPayoutRatioAnnual',
        'NextYearForecastDividendPerShareAnnual'
        ];
        const filteredData = Object.keys(data)
        .filter(key => keysToFilter.includes(key))
        .reduce((obj, key) => {
            obj[key] = data[key];
            return obj;
        }, {});
        console.log('フィルタリング後のデータ:', filteredData);
        //this.$router.push({ name: 'MessagePage', query: { data: JSON.stringify(filteredData) } });
    }
};
</script>
