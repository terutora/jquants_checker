const express = require('express');
const router = express.Router();
const UserController = require('../controllers/UserController');
const StockController = require('../controllers/StockController');

// ユーザー関連のルート
router.get('/users', UserController.getAllUsers);
router.post('/users', UserController.createUser);

// 株式関連のルート
router.get('/stocks', StockController.getAllStocks);
router.post('/stocks', StockController.createStock);

module.exports = router;
