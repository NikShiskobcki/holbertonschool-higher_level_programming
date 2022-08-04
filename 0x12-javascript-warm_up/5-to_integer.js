#!/usr/bin/node

const args = process.argv[2];
const x = parseInt(args);

if (isNaN(x)) {
  console.log('Not a number');
} else {
  console.log('My number:', x);
}
