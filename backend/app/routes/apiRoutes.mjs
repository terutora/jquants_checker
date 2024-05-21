import express from 'express';
const router = express.Router();
const UserController = require('../controllers/UserController.js');
const StockController = require('../controllers/StockController.js');

// ユーザー関連のルート
router.get('/users', UserController.getAllUsers);
router.post('/users', UserController.createUser);

// 株式関連のルート
router.get('/stocks', StockController.getAllStocks);
router.post('/stocks', StockController.createStock);

exports = {router};
