#!/usr/bin/node
const count = process.argv.slice(2);
if (!isNaN(parseInt(count[0], 10))) {
  console.log(`My number: ${parseInt(count[0], 10)}`);
} else {
  console.log('Not a number');
}
