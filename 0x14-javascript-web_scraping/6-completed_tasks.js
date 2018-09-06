#!/usr/bin/node

let request = require('request');
let dct = {};

request(process.argv[2] + '?completed=true', function (err, response, body) {
  if (err) throw err;
  for (let item of JSON.parse(body)) {
    if (dct[item.userId] === undefined) {
      dct[item.userId] = 0;
    }
    dct[item.userId]++;
  }
  console.log(dct);
});
