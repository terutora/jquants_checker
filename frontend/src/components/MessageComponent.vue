<template>
  <div id="app">
    <HeaderComponent />
    <div class="container">
      <main>
        <div>
          <h1 v-if="code">{{ code }}</h1>
          <h2 v-if="infoData">{{ infoData[0].CompanyName }}</h2>
        </div>
        <h3>企業情報</h3>  
        <table v-if="infoData">
          <thead>
            <tr>
              <th>17業種</th>
              <th>33業種</th>
              <th>上場市場</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(company, index) in infoData" :key="index">
              <td>{{ company.Sector17CodeName }}</td>
              <td>{{ company.Sector33CodeName }}</td>
              <td>{{ company.MarketCodeName }}</td>
            </tr>
          </tbody>  
        </table>
    <h3>通期[百万円]</h3>
    <table v-if="tableData">
      <thead>
        <tr>
          <th>決算期</th>
          <th>売上高</th>
          <th>営業利益</th>
          <th>経常利益</th>
          <th>当期純利益</th>
          <th>EPS</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(value, key) in tableData" :key="key">
          <td v-if="value.TypeOfDocument.includes('FY')">{{ value.DisclosedDate }}</td>
          <td v-if="value.TypeOfDocument.includes('FY')">{{ addCommas(value.NetSales.slice(0, -6)) }}</td>
          <td v-if="value.TypeOfDocument.includes('FY')">{{ addCommas(value.OperatingProfit.slice(0, -6)) }}</td>
          <td v-if="value.TypeOfDocument.includes('FY')">{{ addCommas(value.OrdinaryProfit.slice(0, -6)) }}</td>
          <td v-if="value.TypeOfDocument.includes('FY')">{{ addCommas(value.Profit.slice(0, -6)) }}</td>
          <td v-if="value.TypeOfDocument.includes('FY')">{{ value.EarningsPerShare }}</td>
        </tr>
      </tbody>
    </table>

    <h3>四半期別[百万円]</h3>
    <table v-if="tableData">
      <thead>
        <tr>
          <th>決算期</th>
          <th>売上高</th>
          <th>営業利益</th>
          <th>経常利益</th>
          <th>当期純利益</th>
          <th>EPS</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(value, key) in tableData" :key="key">
          <td v-if="value.TypeOfDocument.includes('Q') || value.TypeOfDocument.includes('FY')">{{ value.DisclosedDate }}</td>
          <td v-if="value.TypeOfDocument.includes('Q') || value.TypeOfDocument.includes('FY')">{{ addCommas(value.NetSales.slice(0, -6)) }}</td>
          <td v-if="value.TypeOfDocument.includes('Q') || value.TypeOfDocument.includes('FY')">{{ addCommas(value.OperatingProfit.slice(0, -6)) }}</td>
          <td v-if="value.TypeOfDocument.includes('Q') || value.TypeOfDocument.includes('FY')">{{ addCommas(value.OrdinaryProfit.slice(0, -6)) }}</td>
          <td v-if="value.TypeOfDocument.includes('Q') || value.TypeOfDocument.includes('FY')">{{ addCommas(value.Profit.slice(0, -6)) }}</td>
          <td v-if="value.TypeOfDocument.includes('Q') || value.TypeOfDocument.includes('FY')">{{ value.EarningsPerShare }}</td>
        </tr>
      </tbody>
    </table>    
  </main>
</div>
<footer>
  IR Finder
</footer>
  </div>
</template>
<script>
import HeaderComponent from '@/components/HeaderComponent.vue';
import smoothScroll from '@/assets/js/smoothScroll.js';

export default {
  name: 'MessagePage',
  components: {
    HeaderComponent
  },
  props: {
    code: {
      type: String,
      required: true
    },
    tableData: {
      type: Array,
      required: true
    },
    infoData: {
      type: Array,
      required: true
    }
  },
  mounted() {
    smoothScroll();
  },
  methods:{
    addCommas(value) {
    return value.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ',');
  }
  }
};
</script>
<style>
@import '@/assets/css/main.css';

table {
  width: 100%;
  border-collapse: collapse;
}

th, td {
  border: 1px solid #ddd;
  padding: 8px;
}

th {
  background-color: #f2f2f2;
}
</style>