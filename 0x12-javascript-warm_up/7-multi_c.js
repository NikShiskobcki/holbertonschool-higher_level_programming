#!/usr/bin/node

const m = 'C is fun';
const times = parseInt(process.argv[2]);

if (isNaN(times)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < times; i++) {
    console.log(m);
  }
}
