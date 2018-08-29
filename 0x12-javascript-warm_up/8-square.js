#!/usr/bin/node

let e = parseInt(process.argv[2]);
let x = '';
if (isNaN(e)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < e; i++) {
    for (let y = 0; y < e; y++) {
      x += 'X';
    }
    console.log(x);
    x = '';
  }
}
