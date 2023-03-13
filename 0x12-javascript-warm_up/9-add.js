#!/usr/bin/node
const args = process.argv;

const sum = add(args[2], args[3]);
console.log(sum);
function add (a, b) {
  return Number(a) + Number(b);
}
