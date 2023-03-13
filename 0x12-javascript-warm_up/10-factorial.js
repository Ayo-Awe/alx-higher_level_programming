#!/usr/bin/node
const args = process.argv;

const value = Number(args[2]);
const result = factorial(value);
console.log(result);

function factorial (a) {
  if (isNaN(a) || a === 0 || a === 1) return 1;

  return a * factorial(a - 1);
}
