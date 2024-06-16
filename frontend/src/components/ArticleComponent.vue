<template>
  <div :id="article.id">
    <h2>{{ article.year }}</h2>
    <p>{{ article.text }}</p>
    <img :src="`@/assets/images/${article.img}`"/>
  </div>
</template>

<script>
export default {
  name: 'ArticleComponent',
  props: {
    article: {
      type: Object,
      required: true,
    },
  },
};


</script>

