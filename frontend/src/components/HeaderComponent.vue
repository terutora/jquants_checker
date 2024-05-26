<template>
  <header>
    <div class="logo-search">
      <a href="#">
        <img src="@/assets/images/アセット 1.png" alt="見出し"/>
      </a>
      <form action="/search" method="GET">
        <input id="searchInput" type="text" placeholder="企業コードを入力">
        <button type="submit">検索</button>
      </form>
    </div>
  </header>
</template>

<script>
import search from '@/assets/js/search.js';

export default {
  name: 'HeaderComponent',
  mounted() {
    search();
  },
};
</script>

<style scoped>
/* 必要に応じてスタイルを追加 */
</style>
