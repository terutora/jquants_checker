const mysql = require('mysql2');
const dotenv = require('dotenv');
// 環境変数を読み込む
dotenv.config();

const connection = mysql.createConnection({
  host: process.env.DB_HOST,
  user: process.env.DB_USER,
  password: process.env.DB_PASSWORD,
  database: process.env.DB_NAME,
  ssl: {
    rejectUnauthorized: false,
  }
});

connection.connect(err => {
  if (err) {
    console.error('データベースへの接続エラー:', err);
    return;
  }
  console.log('データベースに接続されました');
});

// 株式関連のコントローラー
class StockController {
  // 株式情報を取得するメソッド
  static getAllStocks(req, res) {
    // データベースから株式情報を取得
    const query = 'SELECT * FROM code_db WHERE LocalCode = ?';
    const filter = req.query.filter;
    console.log("aaaaa");
    connection.query(query, filter, (err, stocks) => {
      if (err) {
        console.error('データ取得エラー:', err);
        res.status(500).json({ error: 'データ取得エラー' });
        return;
      }
      res.json(stocks);
    });
  }

  // 株式情報を取得するメソッド
  static getAllInfo(req, res) {
    // データベースから株式情報を取得
    const query = 'SELECT * FROM basic_info WHERE Code = ?';
    const name = req.query.name;
    console.log("bbbbb")
    connection.query(query, [name], (err, stocks) => {
      if (err) {
        console.error('データ取得エラー:', err);
        res.status(500).json({ error: 'データ取得エラー' });
        return;
      }
      res.json(stocks);
      ;
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

module.exports = StockController;