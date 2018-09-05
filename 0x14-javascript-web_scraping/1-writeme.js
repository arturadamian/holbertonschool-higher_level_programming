#!/usr/bin/node

let fs = require('fs');
fs.appendFile(process.argv[2], process.argv[3], 'utf8', function (err) {
  if (err) throw err;
});
