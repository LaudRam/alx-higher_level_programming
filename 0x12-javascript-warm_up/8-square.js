#!/usr/bin/node

const x = process.argv[2];

if (isNaN(x)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < x; i++) {
    let square = '';
    for (let j = 0; j < x; j++) {
      square += 'X';
    }
    console.log(square);
  }
}
