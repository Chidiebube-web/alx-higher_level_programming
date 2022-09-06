#!/usr/bin/node
if (isNaN(process.argv[2]) || process.argv[2] === undefined) {
  console.log('Missing number of occurrences');
} else {
  const word = 'C is fun';
  for (let i = 0; i < process.argv[2]; i++) {
    console.log(word);
  }
}
