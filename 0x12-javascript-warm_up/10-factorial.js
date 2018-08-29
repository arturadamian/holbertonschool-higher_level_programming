#!/usr/bin/node

let n = Number(process.argv[2]);
let factorial = function (x) {
  if (x === 0 || isNaN(x)) {
    return 1;
  } else {
    return x * factorial(x - 1);
  }
};
console.log(factorial(n));
