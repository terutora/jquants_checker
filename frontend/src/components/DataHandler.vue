<template>
  <div>
    <!-- データの処理は行わず、propsで受け取ったデータをそのままMessagePageに渡す -->
    <MessagePage :code="code" :tableData="tableData" />
  </div>
</template>

<script>
import MessagePage from '@/components/MessageComponent.vue';

export default {
  name: 'DataHandler',
  components: {
    MessagePage
  },
  props: ['code', 'tableData']
};
</script>
