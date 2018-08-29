#!/usr/bin/node

function add (x, y) {
  return x + y;
}

let a = parseInt(process.argv[2]);
let b = parseInt(process.argv[3]);

console.log(add(a, b));
