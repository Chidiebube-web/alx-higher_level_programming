#!/usr/bin/node
let largest = 0;
if (process.argv.length === 0) {
  console.log(0);
} else if (process.argv.length === 1){
  console.log(1);
} else {
  for (i = 0; i < process.argv.length; i++) {
    if (process.argv[i] > largest) {
      largest = process.argv[i] - 1;
    }
  }
}

console.log(largest);
