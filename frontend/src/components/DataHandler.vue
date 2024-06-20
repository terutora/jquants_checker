<template>
  <div>
    <MessagePage :code="code" :table-data="tableData" :info-data="infoData" />
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
      return store.code
    },
    tableData() {
      const store = useStockStore();
      return store.data;
    },
    infoData() {
      const store = useStockStore();
      return store.infoData;
    }
  },
  created() {
    // セッションストレージからデータを取得
    const data = JSON.parse(sessionStorage.getItem('data'));
    const infoData = JSON.parse(sessionStorage.getItem('infoData'));
    const code = sessionStorage.getItem('code');
    if (data && code) {
      const store = useStockStore();
      store.data = data;
      store.code = code;
    }
    if (infoData) {
      const store = useStockStore();
      store.infoData = infoData;
    }
  }
};
</script>
