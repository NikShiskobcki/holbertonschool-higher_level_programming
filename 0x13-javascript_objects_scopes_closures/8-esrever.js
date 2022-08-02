#!/usr/bin/node

exports.esrever = function (list) {
  const aux = [];
  for (let i = list.lenght - 1; i >= 0; i--) {
    aux.push(list[i]);
  }
  return aux;
};
