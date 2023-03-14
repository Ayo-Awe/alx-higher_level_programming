#!/usr/bin/node
const fs = require("fs");
const args = process.argv.slice(2);

const fileOne = fs.readFileSync(args[0]).toString();
const fileTwo = fs.readFileSync(args[1]).toString();

fs.writeFileSync(args[2], fileOne + fileTwo);
