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
import HeaderComponent from './components/HeaderComponent.vue';
import NavigationComponent from './components/NavigationComponent.vue';
import ArticleComponent from './components/ArticleComponent.vue';

export default {
  name: 'App',
  components: {
    HeaderComponent,
    NavigationComponent,
    ArticleComponent,
  },
  data() {
    return {
      articles: [
        { id: '2024', year: '2024年', text: '成長企業といえば', img: 'src/assets/images/copy1.jpg' },
        { id: '2023', year: '2023年', text: 'おすすめの半導体銘柄', img: 'src/assets/images/copy2.jpg' },
        { id: '2022', year: '2022年', text: '今年はやりそうな業種', img: 'src/assets/images/copy3.jpg' },
      ],
    };
  },
};
</script>

<style>
@import './assets/css/main.css';
</style>
