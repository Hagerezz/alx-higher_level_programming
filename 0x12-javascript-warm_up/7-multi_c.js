#!/usr/bin/node
let i = 0;
const count = process.argv[2];
if (!isNaN(parseInt(count, 10))) {
  while (i < count) {
    console.log('C is fun');
    i++;
  }
} else {
  console.log('Missing number of occurrences');
}
