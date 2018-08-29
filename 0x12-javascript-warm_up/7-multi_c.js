#!/usr/bin/node

let e = parseInt(process.argv[2]);
if (isNaN(e)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < e; ++i) {
    console.log('C is fun');
  }
}
