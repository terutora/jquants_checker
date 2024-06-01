<template>
  <header>
    <div class="logo-search">
      <a href="#">
        <img :src="logo" alt="見出し"/>
      </a>
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
        const modifiedKeyword = `${this.keyword}0`
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
          // Optional: ここで他の処理を行う（例：ページ遷移、データ表示など）
          this.$router.push({ name: 'MessagePage', query: { data: JSON.stringify(data) } });
        } else {
          this.message = '';  // 通常メッセージをクリア
          console.log('コードが見つかりませんでした');
          alert(this.errorMessage);  // アラートでエラーメッセージを表示
        }
      } catch (error) {
        console.error('データの取得エラー:', error);
        this.errorMessage = 'エラーが発生しました';
        console.log('ErrorPageルートに遷移します');
        // Optional: エラーページに遷移したくない場合は以下の行をコメントアウトまたは削除
        // this.$router.push({ name: 'ErrorPage' });
        alert(this.errorMessage);  // アラートでエラーメッセージを表示
      }
    }
  }
};
</script>