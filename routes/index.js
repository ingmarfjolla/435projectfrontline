var express = require('express');
var router = express.Router();
var db=require('../database');

/* GET home page. */
// router.get('/', function(req, res, next) {
//   res.render('index', { title: 'Express',data: data });
// });
router.get('/', function(req, res, next) {
  var sql='SELECT * FROM FRONTLINE';
  db.query(sql, function (err, data, fields) {
  if (err) throw err;
  res.render('index', { title: 'index',data: data});
});
});

module.exports = router;
