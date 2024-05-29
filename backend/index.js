const express = require('express');
const config = require('./config/config.js');
const userRoutes = require('./app/routes/apiRoutes.js');

const app = express();
const cors = require('cors');

// CORSの設定
app.use(cors());

// ミドルウェアの設定やルーティングの設定
app.use('/api', userRoutes);

// サーバーを起動
const PORT = config.port || 4000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
