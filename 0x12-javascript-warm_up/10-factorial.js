#!/usr/bin/node
function factorial (r) {
  if (r < 0) {
    return (-1);
  }
  if (r === 0 || isNaN(r)) {
    return (1);
  }
  return (r * factorial(r - 1));
}

console.log(factorial(Number(process.argv[2])));
