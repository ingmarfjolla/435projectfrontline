var express = require('express');
var router = express.Router();
var db=require('../database');

/* GET home page. */
// router.get('/', function(req, res, next) {
//   res.render('trymee', { title: 'Expraaaess' });
// });
router.get('/', function(req, res, next) {
    var sql='SELECT * FROM FRONTLINE';
    db.query(sql, function (err, data, fields) {
    if (err) throw err;
    res.render('trymee', { title: 'frontline',data: data});
  });
});
module.exports = router;
