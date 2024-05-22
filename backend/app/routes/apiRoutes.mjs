import express from 'express';
import { UserController } from '../controllers/UserController.mjs';
import { StockController } from '../controllers/StockController.mjs';

const router = express.Router();

// ユーザー関連のルート
router.get('/users', UserController.getAllUsers);
router.post('/users', UserController.createUser);

// 株式関連のルート
router.get('/stocks', StockController.getAllStocks);
router.post('/stocks', StockController.createStock);

export { router };
