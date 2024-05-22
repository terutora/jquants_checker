import express from 'express';
import mysql from 'mysql';
import dotenv from 'dotenv';

dotenv.config();

const connection = mysql.createConnection({
  host: process.env.DB_HOST,
  user: process.env.DB_USER,
  password: process.env.DATABASE_PASSWORD,
  database: process.env.DB_NAME
});

connection.connect(err => {
  if (err) {
    console.error('データベースへの接続エラー:', err);
    return;
  }
  console.log('データベースに接続されました');
});

// ルーターを作成
const router = express.Router();

// 株式関連のコントローラー
export class StockController {
  // 株式情報を取得するメソッド
  static getAllStocks(req, res) {
    // データベースから株式情報を取得
    const query = 'SELECT * FROM code_db WHERE LocalCode = ?';
    const filter = req.query.filter;

    connection.query(query, [filter], (err, stocks) => {
      if (err) {
        console.error('データ取得エラー:', err);
        res.status(500).json({ error: 'データ取得エラー' });
        return;
      }
      res.json(stocks);
    });
  }

  // 株式情報を作成するメソッド
  static createStock(req, res) {
    // リクエストボディから株式情報を取得
    const stock = req.body;

    // データベースに株式情報を追加
    const query = 'INSERT INTO code_db SET ?';
    connection.query(query, stock, (err, result) => {
      if (err) {
        console.error('データ追加エラー:', err);
        res.status(500).json({ error: 'データ追加エラー' });
        return;
      }
      res.json({ message: '株式情報を追加しました' });
    });
  }
}

// ルーターをエクスポート
export default router;
