<template>
  <header>
    <div class="logo-search">
      <router-link to="/">
        <img :src="logo" alt="見出し"/>
      </router-link>
      <form @submit.prevent="handleSubmit">
        <input id="searchInput" v-model="keyword" type="text" placeholder="企業コードを入力">
        <button type="submit">検索</button>
      </form>
    </div>
  </header>
</template>

<script>
import axios from 'axios';
import logoImage from '@/assets/images/アセット 1.png';

export default {
  name: 'HeaderComponent',
  data() {
    return {
      keyword: '',
      message: '',
      errorMessage: 'コードが見つかりませんでした',
      logo: logoImage
    };
  },
  methods: {
    async handleSubmit() {
      try {
        console.log('キーワード:', this.keyword);
        const modifiedKeyword = `${this.keyword}0`;
        console.log('修正後のキーワード:', modifiedKeyword);
        const response = await axios.get('http://localhost:4000/api/stocks', {
          params: {
            filter: modifiedKeyword
          }
        });
        console.log('レスポンス:', response.data);

        const data = response.data;
        if (data && Object.keys(data).length > 0) {
          this.message = data.message;
          console.log('メッセージルートに遷移します');
          // セッションストレージにデータを保存
          sessionStorage.setItem('data', JSON.stringify(data));
          sessionStorage.setItem('code', this.keyword);
          this.$router.push({ name: 'DataHandler' });
        } else {
          this.message = '';  // 通常メッセージをクリア
          console.log('コードが見つかりませんでした');
          alert(this.errorMessage);  // アラートでエラーメッセージを表示
        }
      } catch (error) {
        console.error('データの取得エラー:', error);
        this.errorMessage = 'エラーが発生しました';
        alert(this.errorMessage);  // アラートでエラーメッセージを表示
      }
    }
  }
};
</script>
