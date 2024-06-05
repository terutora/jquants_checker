import { defineStore } from 'pinia';
import axios from 'axios';

export const useStockStore = defineStore('stocks', {
  state: () => ({
    code: '',
    data: null,
    errorMessage: 'コードが見つかりませんでした'
  }),
  actions: {
    async fetchData(keyword) {
      try {
        const modifiedKeyword = `${keyword}0`;
        const response = await axios.get('http://localhost:4000/api/stocks', {
          params: {
            filter: modifiedKeyword
          }
        });
        const data = response.data;
        if (data && Object.keys(data).length > 0) {
          this.data = data;
          this.code = keyword;
          sessionStorage.setItem('data', JSON.stringify(data));
          sessionStorage.setItem('code', keyword);
        } else {
          this.errorMessage = 'コードが見つかりませんでした';
          alert(this.errorMessage);
        }
      } catch (error) {
        this.errorMessage = 'エラーが発生しました';
        alert(this.errorMessage);
      }
    }
  }
});
