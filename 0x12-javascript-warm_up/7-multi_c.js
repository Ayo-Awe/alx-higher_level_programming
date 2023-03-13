#!/usr/bin/node
const args = process.argv;
const myNumber = Number(args[2]);
// Test for NaN
if (isNaN(myNumber)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < myNumber; i++) console.log('C is fun');
}
