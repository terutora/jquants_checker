const express = require('express');
const userRoutes = require('./app/routes/apiRoutes.js');
const path = require('path');
const app = express();
const cors = require('cors');

app.use(express.static(path.join(__dirname, '../my-app/build')));

// CORSの設定
app.use(cors());

// ミドルウェアの設定やルーティングの設定
app.use('/api', userRoutes);

app.get("/un", (req, res) => {
  res.json({ message: "Hello World!" });
});

app.get('*', (req, res) => {
  res.sendFile(path.join(__dirname,'../my-app/build/index.html'));
});

// サーバーを起動
const PORT = process.env.PORT || 4000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
