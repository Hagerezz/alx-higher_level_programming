#!/usr/bin/node
let i = 0;
const args = process.argv[2];
const check = parseInt(args, 10);
if (!isNaN(check)) {
  while (i < args) {
    console.log('C is fun');
    i++;
  }
} else {
  console.log('Missing number of occurrences');
}
