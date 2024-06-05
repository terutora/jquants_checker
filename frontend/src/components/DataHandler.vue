<template>
  <div>
    <MessagePage :code="code" :table-data="tableData" />
  </div>
</template>

<script>
import { useStockStore } from '@/stores/stocks';
import MessagePage from '@/components/MessageComponent.vue';

export default {
  name: 'DataHandler',
  components: {
    MessagePage
  },
  computed: {
    code() {
      const store = useStockStore();
      return store.code;
    },
    tableData() {
      const store = useStockStore();
      return store.data;
    }
  },
  created() {
    // セッションストレージからデータを取得
    const data = JSON.parse(sessionStorage.getItem('data'));
    const code = sessionStorage.getItem('code');
    if (data && code) {
      const store = useStockStore();
      store.data = data;
      store.code = code;
    }
  }
};
</script>
