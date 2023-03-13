#!/usr/bin/node
const args = process.argv;
const myNumber = Number(args[2]);
// Test for NaN
if (isNaN(myNumber)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < myNumber; i++) {
    const row = 'X'.repeat(myNumber);
    console.log(row);
  }
}
