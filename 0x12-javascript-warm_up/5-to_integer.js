#!/usr/bin/node

let e = parseInt(process.argv[2]);
if (isNaN(e)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + e);
}
