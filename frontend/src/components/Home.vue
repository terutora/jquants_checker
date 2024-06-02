<template>
  <div id="app">
    <HeaderComponent />
    <div class="container">
      <NavigationComponent />
      <main>
        <ArticleComponent
          v-for="article in articles"
          :key="article.id"
          :article="article"
        />
      </main>
    </div>
    <footer>
      IR Finder
    </footer>
  </div>
</template>

<script>
import HeaderComponent from '@/components/HeaderComponent.vue';
import NavigationComponent from '@/components/NavigationComponent.vue';
import ArticleComponent from '@/components/ArticleComponent.vue';

import smoothScroll from '@/assets/js/smoothScroll.js';


export default {
  name: 'HomePage',
  components: {
    HeaderComponent,
    NavigationComponent,
    ArticleComponent,
  },
  data() {
    return {
      articles: [
        { id: '2024', year: '2024年', text: '成長企業といえば', img: 'copy1.jpg' },
        { id: '2023', year: '2023年', text: 'おすすめの半導体銘柄', img: 'copy2.jpg' },
        { id: '2022', year: '2022年', text: '今年はやりそうな業種', img: 'copy3.jpg' },
      ],
    };
  },
  mounted() {
    smoothScroll();
  },
};
</script>

<style>
@import '@/assets/css/main.css';
</style>
  