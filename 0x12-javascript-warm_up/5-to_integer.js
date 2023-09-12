#!/usr/bin/node
const args = process.argv[2];
const check = parseInt(args, 10);
if (!isNaN(check)) {
  console.log(`My number: ${check}`);
} else {
  console.log('Not a number');
}
