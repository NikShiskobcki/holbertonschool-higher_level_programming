#!/usr/bin/node

const args = process.argv.slice(2);
const fs = require('fs');
const data = args[1];
fs.writeFile(args[0], data, err => {
  if (err) {
    console.error(err);
  }
});
