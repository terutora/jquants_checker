// UserController.mjs

// クラスを使う場合
export class UserController {
  static getAllUsers(req, res) {
    // 実際の処理
    res.send('All users');
  }

  static createUser(req, res) {
    // 実際の処理
    res.send('User created');
  }
}
