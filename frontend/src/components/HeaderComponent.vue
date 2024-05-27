// src/components/HeaderComponent.vue

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
        console.log('Keyword:', this.keyword);  // デバッグ用
        const response = await axios.get('/api/data', {
          params: {
            filter: this.keyword
          }
        });
        console.log('Response:', response.data);  // デバッグ用
        const data = response.data;
        if (data) {
          window.location.href = `${this.keyword}.html`;
        } else {
          alert('該当するページが見つかりません。');
        }
      } catch (error) {
        console.error('Error fetching data:', error);
        alert('エラーが発生しました。');
      }
    }
  }
}
</script>

<template>
  <div>
    <input v-model="keyword" placeholder="キーワードを入力">
    <button @click="handleSubmit">送信</button>
  </div>
</template>
