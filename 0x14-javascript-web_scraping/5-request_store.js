#!/usr/bin/node

let request = require('request');
let fs = require('fs');

request(process.argv[2], function (err, response, body) {
  if (err) throw err;
  fs.writeFile(process.argv[3], body, 'utf8', function (err) {
    if (err) throw err;
  });
});
