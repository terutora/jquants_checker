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
        // まずは http://localhost:4000/api/stocks に対してリクエストを送信し、データを取得する
        const response = await axios.get('https://irfinder-39e9cd03a7da.herokuapp.com/api/stocks', {
          params: {
            filter: modifiedKeyword
          }
        });
        const data = response.data;
    
        // 次に http://localhost:4000/api/info に対してリクエストを送信し、追加の情報を取得する
        const infoResponse = await axios.get('https://irfinder-39e9cd03a7da.herokuapp.com/api/info', {
          params: {
            name: modifiedKeyword
          }
        });
        const infoData = infoResponse.data;
    
        if (data && Object.keys(data).length > 0 && infoData && Object.keys(infoData).length > 0) {
          this.data = data;
          this.code = keyword;
          sessionStorage.setItem('data', JSON.stringify(data));
          sessionStorage.setItem('code', keyword);
    
          // infoDataもセッションストレージに保存する
          sessionStorage.setItem('infoData', JSON.stringify(infoData));
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
