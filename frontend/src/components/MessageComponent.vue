<template>
  <div id="app">
    <HeaderComponent />
    <div class="container">
      <main>
        <table v-if="tableData">
          <thead>
            <tr>
              <th>項目</th>
              <th>値</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(value, key) in tableData" :key="key">
              <td>{{ key }}</td>
              <td>{{ value }}</td>
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
  data() {
    return {
      tableData: null
    };
  },
  created() {
    if (this.$route.query.data) {
      this.tableData = JSON.parse(this.$route.query.data);
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
