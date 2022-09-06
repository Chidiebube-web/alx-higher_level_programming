#!/usr/bin/node
const x = Number(process.argv[2]);
function recursive (y) {
  if (isNaN(y) || y === 0) {
    return (1);
  } else if ( y < 0) {
    return (-1);
  } else {
    return (y * recursive(y - 1));
  }
}

console.log(recursive(x));
