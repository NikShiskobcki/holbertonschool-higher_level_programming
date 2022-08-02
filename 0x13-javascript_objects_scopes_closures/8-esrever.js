#!/usr/bin/node

exports.esrever = function (list) {
  const aux = [];
  for (let i = list.lenght; i > 0; i--) {
    aux.push(list[i]);
  }
  return aux;
};
