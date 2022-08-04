#!/usr/bin/node

exports.converter = function (base) {
  function change (num) {
    return num.toString(base);
  }
  return change;
};
