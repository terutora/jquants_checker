const express = require('express');
const userRoutes = require('./app/routes/apiRoutes.js');
const path = require('path');
const app = express();
const cors = require('cors');

// CORSの設定
app.use(cors());

// ミドルウェアの設定やルーティングの設定
app.use('/api', userRoutes);

// 静的ファイルの設定
app.use(express.static(path.join(__dirname, '../frontend/dist')));

// その他のリクエストに対してはindex.htmlを返す
app.get('*', (req, res) => {
  res.sendFile(path.join(__dirname,'../frontend/dist/index.html'));
});

// サーバーを起動
const PORT = process.env.PORT || 4000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
