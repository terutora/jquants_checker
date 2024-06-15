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
import logoImage from '@/assets/images/アセット 1.png';
import { useStockStore } from '@/stores/stocks';

export default {
  name: 'HeaderComponent',
  data() {
    return {
      keyword: '',
      logo: logoImage
    };
  },
  methods: {
    async handleSubmit() {
      const store = useStockStore();
      await store.fetchData(this.keyword);
      this.$router.push({ name: 'DataHandler' });
    }
  }
};
</script>
