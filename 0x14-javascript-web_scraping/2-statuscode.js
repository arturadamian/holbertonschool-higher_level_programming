#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (err, code) {
  if (err) throw err;
  console.log('code: ' + code.statusCode);
});
