#!/usr/bin/node
const count = process.argv.slice(2);
if (count[0]) {
  console.log(count[0]);
} else {
  console.log('No argument');
}