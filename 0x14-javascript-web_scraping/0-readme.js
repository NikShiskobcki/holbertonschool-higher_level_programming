#!/usr/bin/node

const args = process.argv.slice(2);
const fs = require('fs');
fs.readFile(args[0], 'utf-8', (err, inputD) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(inputD);
});
