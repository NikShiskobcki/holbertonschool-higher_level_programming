#!/usr/bin/node

let argP = 0;
exports.logMe = function (item) {
  console.log(argP + ': ' + item);
  argP++;
};
