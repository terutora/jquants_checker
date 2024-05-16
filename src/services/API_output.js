const express = require('express');
const mysql = require('mysql');
const basicAuth = require('express-basic-auth');

const app = express();
const port = process.env.PORT || 4000;

// CORSミドルウェアの設定
app.use(function(req, res, next) {
  res.header("Access-Control-Allow-Origin", "*"); // すべてのオリジンからアクセスを許可
  res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
  next();
});

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

// Basic認証の設定
app.use(basicAuth({
  users: { admin: process.env.BASIC_AUTH_PASSWORD }, // ユーザー名とパスワードを環境変数から読み込む
  challenge: true,
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
  console.log(`サーバーは http://localhost:${port}/users で動作中です`);
});
