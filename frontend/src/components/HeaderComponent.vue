<template>
  <div>
    <input v-model="keyword" placeholder="キーワードを入力">
    <button @click="handleSubmit">送信</button>
    <p>{{ message }}</p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      keyword: '',
      message: ''
    };
  },
  methods: {
    async handleSubmit() {
      try {
        console.log('キーワード:', this.keyword);
        const response = await axios.get('http://localhost:4000/api/stocks', {
          params: {
            filter: this.keyword
          }
        });
        console.log('レスポンス:', response.data);
        const data = response.data;
        if (data.message) {
          this.message = data.message;  // デバッグ用に追加
          console.log('メッセージルートに遷移します');
          this.$router.push({ name: 'Message', query: { message: data.message } });
        } else {
          console.log('NotFoundルートに遷移します');
          this.$router.push({ name: 'NotFound' });
        }
      } catch (error) {
        console.error('データの取得エラー:', error);
        console.log('ErrorPageルートに遷移します');
        this.$router.push({ name: 'ErrorPage' });
      }
    }
  }
}
</script>
