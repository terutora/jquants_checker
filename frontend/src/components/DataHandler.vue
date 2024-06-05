<template>
  <div>
    <!-- データの処理は行わず、propsで受け取ったデータをそのままMessagePageに渡す -->
    <MessagePage :code="code" :table-data="tableData" />
  </div>
</template>

<script>
import MessagePage from '@/components/MessageComponent.vue';

export default {
  name: 'DataHandler',
  components: {
    MessagePage
  },
  data() {
    return {
      code: '',
      tableData: null
    };
  },
  created() {
    // セッションストレージからデータを取得
    const data = JSON.parse(sessionStorage.getItem('data'));
    this.code = sessionStorage.getItem('code');
    this.tableData = data;
  }
};
</script>
