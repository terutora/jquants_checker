// 必要なモジュールをインポート
import express from 'express';
import { config } from './config/config.mjs';
import { router as userRoutes } from './app/routes/apiRoutes.mjs';

const app = express();

// ミドルウェアの設定やルーティングの設定
app.use('/api', userRoutes);

// サーバーを起動
const PORT = config.port || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
