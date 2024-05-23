<template>
  <article :id="article.id">
    <h2>{{ article.year }}</h2>
    <p>{{ article.text }}</p>
    <img :src="`@/assets/images/${article.img}`" :alt="article.id">
  </article>
</template>

<script>
export default {
  name: 'ArticleComponent',
  props: {
    article: Object,
  },
};
</script>

<style scoped>
/* 必要に応じてスタイルを追加 */
</style>
