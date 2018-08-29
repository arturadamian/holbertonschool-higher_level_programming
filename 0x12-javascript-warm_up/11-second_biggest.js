#!/usr/bin/node

function secondMax (x) {
  return x.sort().reverse()[1];
}
if (process.argv.length < 4) {
  console.log('0');
} else {
  console.log(secondMax(process.argv.slice(2)));
}
