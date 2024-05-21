// 必要なモジュールをインポート
const express = require('express');
const app = express();
const userRoutes = require('./app/routes/apiRoutes');
const config = require('./config/config');

// ミドルウェアの設定やルーティングの設定
app.use('/api', userRoutes);

// サーバーを起動
const PORT = config.port || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
