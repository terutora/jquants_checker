<template>
  <div>
    <h1>メッセージ</h1>
    <p>{{ message }}</p>
    <table v-if="tableData.length" class="table-bordered">
      <thead>
        <tr>
          <th v-for="(value, key) in tableData[0]" :key="key">{{ key }}</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(row, index) in tableData" :key="index">
          <td v-for="(value, key) in row" :key="key">{{ value }}</td>
        </tr>
      </tbody>
    </table>
    <p v-else>データがありません</p>
  </div>
</template>

<script>
export default {
  name: 'MessagePage',
  data() {
    return {
      message: '',
      tableData: []
    };
  },
  created() {
    this.message = this.$route.query.message || '';
    if (this.$route.query.data) {
      this.tableData = JSON.parse(this.$route.query.data);
    }
  }
};
</script>

<style scoped>
.table-bordered {
  border-collapse: collapse;
}

.table-bordered th,
.table-bordered td {
  border: 1px solid #ddd;
  padding: 8px;
}
</style>
