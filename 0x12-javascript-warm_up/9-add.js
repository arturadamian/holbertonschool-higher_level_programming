#!/usr/bin/node

let a = parseInt(process.argv[2]);
let b = parseInt(process.argv[3]);
function add (x, y) {
    return x + y;
}
if (isNaN(a) || isNaN(b)) {
    console.log('NAN');
} else {
    console.log(add(a, b));
}
