#!/usr/bin/node

exports.esrever = function (list) {
  const aux = [];
  for (let i = list.length - 1; i >= 0; i--) {
    aux.push(list[i]);
  }
  return aux;
};
