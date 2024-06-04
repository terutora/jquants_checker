<template>
    <!-- DataHandlerコンポーネントにcodeとtableDataを渡して利用する -->
    <DataHandler :code="receivedCode" :tableData="receivedTableData" />
  </template>
  
  <script>
  import DataHandler from '@/components/DataHandler.vue';
  
  export default {
    components: {
      DataHandler
    },
    data() {
      return {
        receivedCode: '123', // 受け取るデータの例として123という値を設定
        receivedTableData: { /* 受け取るテーブルデータの例 */ }
      };
    }
  };
  </script>
  