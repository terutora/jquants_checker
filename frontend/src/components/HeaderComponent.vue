<template>
  <header>
    <div class="logo-search">
      <a href="#">
        <img src="@/assets/images/アセット 1.png" alt="見出し"/>
      </a>
      <form action="/search" method="GET">
        <input type="text" id="searchInput" placeholder="企業コードを入力">
        <button type="submit">検索</button>
      </form>
    </div>
  </header>
</template>

<script>
export default {
  name: 'HeaderComponent',
};
</script>

<style scoped>
/* 必要に応じてスタイルを追加 */
</style>
