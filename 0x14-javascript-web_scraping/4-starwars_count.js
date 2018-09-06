#!/usr/bin/node

const request = require('request');
let count = 0;

request(process.argv[2], function (err, response, body) {
  if (err) throw err;
  let results = JSON.parse(body).results;
  for (let item of results) {
    for (let actor of item.characters) {
      if (actor.endsWith('18/')) {
        count++;
      }
    }
  }
  console.log(count);
});
