#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let count = list.reduce(function (n, val) {
    return n + (val === searchElement);
  }, 0);
  return count;
};
