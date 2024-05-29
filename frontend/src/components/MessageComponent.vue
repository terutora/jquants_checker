<!-- components/MessageComponent.vue -->
<template>
    <div>
      <h1>新しいページ</h1>
      <p>{{ message }}</p>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        message: '表示するメッセージ'  // メッセージをデータとして持つ
      };
    }
  }
  </script>
  
  <style scoped>
  /* スタイルを記述 */
  </style>
  