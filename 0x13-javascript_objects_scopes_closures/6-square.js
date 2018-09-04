#!/usr/bin/node

const oldSquare = require('./5-square');

module.exports = class Square extends oldSquare {
  charPrint (c) {
    for (let i = 0; i < this.height; ++i) {
      if (c === undefined) {
        c = 'X';
      }
      console.log(c.repeat(this.width));
    }
  }
};
