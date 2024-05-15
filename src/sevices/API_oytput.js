// 必要なモジュールをインポート
const express = require('express');
const mysql = require('mysql');
const app = express();
const port = 3000;

// MySQLデータベース接続設定
const connection = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: '',
  database: 'mydatabase'
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
app.get('/users', (req, res) => {
  connection.query('SELECT * FROM users', (err, results) => {
    if (err) {
      res.status(500).json({ error: 'データ取得エラー' });
      return;
    }
    res.json(results);
  });
});

// サーバーを起動
app.listen(port, () => {
  console.log(`サーバーは http://localhost:${port} で動作中です`);
});
