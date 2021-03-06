#!/usr/bin/node

const request = require('request');

request('http://swapi.co/api/films/' + process.argv[2], function (err, response, body) {
  if (err) throw err;
  for (let actor of JSON.parse(body).characters) {
    request(actor, function (err, response, body) {
      if (err) throw err;
      console.log(JSON.parse(body).name);
    });
  }
});
