const express = require('express');
const mysql = require('mysql');
const router = express.Router();

require('dotenv').config();

// MySQLデータベース接続設定
const connection = mysql.createConnection({
  host: process.env.DB_HOST,
  user: process.env.DB_USER,
  password: process.env.DATABASE_PASSWORD, // パスワードを環境変数から読み込む
  database: process.env.DB_NAME
});

// データベースに接続
connection.connect(err => {
  if (err) {
    console.error('データベースへの接続エラー:', err);
    return;
  }
  console.log('データベースに接続されました');
});

// ユーザー情報を取得するAPIエンドポイント
router.get('/stocks', (req, res) => {
  const query = 'SELECT * FROM code_db WHERE LocalCode = ?';
  const filter = req.query.filter;

  connection.query(query, [filter], (err, stocks) => {
    if (err) {
      res.status(500).json({ error: 'データ取得エラー' });
      return;
    }
    res.json(stocks);
  });
});

module.exports = router;