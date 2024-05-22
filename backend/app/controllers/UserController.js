// UserController.mjs

// クラスを使う場合
class UserController {
  static getAllUsers(req, res) {
    // 実際の処理
    res.send('All users');
  }

  static createUser(req, res) {
    // 実際の処理
    res.send('User created');
  }
}

module.exports = UserController;
