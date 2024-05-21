// 必要なモジュールをインポート
import express from 'express';
import { router as userRoutes } from './app/routes/apiRoutes.mjs';

// const app = express(); この行は移動してください

// expressアプリケーションのインスタンスを生成
const app = express();

// ミドルウェアの設定やルーティングの設定
app.use('/api', userRoutes);

// サーバーを起動
const PORT = config.port || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
