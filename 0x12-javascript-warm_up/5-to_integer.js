#!/usr/bin/node
const args = process.argv;

const myNumber = Number(args[2]);
// Test for NaN
if (isNaN(myNumber)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${myNumber}`);
}
