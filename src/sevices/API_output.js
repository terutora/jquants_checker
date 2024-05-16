const express = require('express');
const mysql = require('mysql');
const basicAuth = require('express-basic-auth');

const app = express();
const port = 3000;

// MySQLデータベース接続設定
const connection = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: process.env.DATABASE_PASSWORD, // パスワードを環境変数から読み込む
  database: 'info_db'
});

// データベースに接続
connection.connect(err => {
  if (err) {
    console.error('データベースへの接続エラー:', err);
    return;
  }
  console.log('データベースに接続されました');
});

// ベーシック認証を追加
app.use(basicAuth({
  users: { 'admin': 'supersecret' }, // ユーザー名とパスワードの組み合わせ
  unauthorizedResponse: { error: '認証エラー' }
}));

// ユーザー情報を取得するAPIエンドポイント
app.get('/users', (req, res) => {
  // LocalCodeが13010のレコードを取得するクエリ
  const query = 'SELECT * FROM code_db WHERE LocalCode = ?';
  const localCode = 13010;

  connection.query(query, [localCode], (err, results) => {
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
