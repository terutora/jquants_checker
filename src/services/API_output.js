const express = require('express');
const app = express();
const mysql = require('mysql');
const cors = require('cors')
const port = process.env.PORT || 4000;

app.use(cors())
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

// ユーザー情報を取得するAPIエンドポイント
app.get('/', (req, res) => {
  // LocalCodeが13010のレコードを取得するクエリ
  const query = 'SELECT * FROM code_db WHERE LocalCode = ?';
  const filter = req.query.filter;

  connection.query(query, [filter], (err, results) => {
    if (err) {
      res.status(500).json({ error: 'データ取得エラー' });
      return;
    }
    res.json(results);
  });
});

// サーバーを起動
app.listen(port, () => {
  console.log(`サーバーは http://localhost:${port}/ で動作中です`);
});
