const express = require('express');
const UserController = require('../controllers/UserController.js');
const StockController = require('../controllers/StockController.js');

const router = express.Router();

// ユーザー関連のルート
router.get('/users', UserController.getAllUsers);
router.post('/users', UserController.createUser);

// 株式関連のルート
router.get('/stocks', StockController.getAllStocks);
router.post('/stocks', StockController.createStock);

// 新しいエンドポイントを追加
router.get('/info', StockController.getAllInfo);

module.exports = router;
