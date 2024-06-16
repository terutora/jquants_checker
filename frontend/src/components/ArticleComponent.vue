<template>
  <div :id="article.id">
    <h2>{{ article.year }}</h2>
    <p>{{ article.text }}</p>
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

