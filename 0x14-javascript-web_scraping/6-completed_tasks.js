#!/usr/bin/node

let request = require('request');
let i = 1;
let count = 0;
let dct = {};

request(process.argv[2] + '?completed=true', function (err, response, body) {
  if (err) throw err;
  for (let item of JSON.parse(body)) {
    if (i === item.userId) {
      ++count;
    } else {
      i++;
      count = 1;
    }
    dct[i] = count;
  }
  console.log(dct);
});
