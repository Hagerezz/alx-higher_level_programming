#!/usr/bin/node
const count = process.argv[2];
if (!isNaN(parseInt(count, 10))) {
  for (let i = 0; i < count; i++) {
    let row = '';
    for (let j = 0; j < count; j++) {
      row += 'X';
    }
    console.log(row);
  }
} else {
  console.log('Missing size');
}
