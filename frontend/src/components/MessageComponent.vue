<template>
  <div id="app">
    <HeaderComponent />
    <div class="container">
      <main>
        <h1 v-if="code">{{ code }}</h1>
        <h3>通期</h3>
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
              <td v-if="value.TypeOfDocument.includes('FY')">{{ value.NetSales }}</td>
              <td v-if="value.TypeOfDocument.includes('FY')">{{ value.OperatingProfit }}</td>
              <td v-if="value.TypeOfDocument.includes('FY')">{{ value.OrdinaryProfit }}</td>
              <td v-if="value.TypeOfDocument.includes('FY')">{{ value.Profit }}</td>
              <td v-if="value.TypeOfDocument.includes('FY')">{{ value.EarningsPerShare }}</td>
            </tr>
          </tbody>
        </table>

        <h3>四半期別</h3>
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
              <td v-if="value.TypeOfDocument.includes('Q') || value.TypeOfDocument.includes('FY')">{{ value.NetSales }}</td>
              <td v-if="value.TypeOfDocument.includes('Q') || value.TypeOfDocument.includes('FY')">{{ value.OperatingProfit }}</td>
              <td v-if="value.TypeOfDocument.includes('Q') || value.TypeOfDocument.includes('FY')">{{ value.OrdinaryProfit }}</td>
              <td v-if="value.TypeOfDocument.includes('Q') || value.TypeOfDocument.includes('FY')">{{ value.Profit }}</td>
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
    }
  },
  mounted() {
    smoothScroll();
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
