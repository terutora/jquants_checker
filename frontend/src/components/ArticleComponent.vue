<template>
  <div :id="article.id">
    <h2>{{ article.year }}</h2>
    <p>{{ article.text }}</p>
    <ul>
      <li v-for="tag in article.tags" :key="tag.id">{{ tag.name }}</li>
    </ul>
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

