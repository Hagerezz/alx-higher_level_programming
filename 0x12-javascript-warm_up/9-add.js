#!/usr/bin/node
const first = Number(process.argv[2]);
const second = Number(process.argv[3]);
function add (a, b) {
  const sum = a + b;
  console.log(sum);
}
add(first, second);
