const express = require('express');
const router = express.Router();

router.get('/users', (req, res) => {
  const users = [
    { id: 1, name: 'Alice' },
    { id: 2, name: 'Bob' },
  ];
  res.json(users);
});

module.exports = router;
