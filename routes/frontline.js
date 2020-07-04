var express = require('express');
var router = express.Router();
var db=require('../database');
// another routes also appear here
// this script to fetch data from MySQL databse table
router.get('/', function(req, res, next) {
    var sql='SELECT * FROM FRONTLINE';
    db.query(sql, function (err, data, fields) {
    if (err) throw err;
    res.render('frontline', { title: 'frontline',data: data});
  });
});
/* GET home page. */
// router.get('/', function(req, res, next) {
//   res.render('index', { title: 'Express' });
// });
module.exports = router;
