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
      keyword: ''
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
          // メッセージを新しいページに表示するために遷移
          this.$router.push({ name: 'Message', query: { message: data.message } });
        } else {
          this.$router.push({ name: 'NotFound' }); // メッセージがない場合は404ページに遷移
        }
      } catch (error) {
        console.error('データの取得エラー:', error);
        this.$router.push({ name: 'Error' }); // エラーが発生した場合はエラーページに遷移
      }
    }
  }
}
</script>
