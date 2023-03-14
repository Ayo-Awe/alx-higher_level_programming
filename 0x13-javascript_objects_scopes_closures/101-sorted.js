#!/usr/bin/node
const { dict } = require('./101-data.js');

const result = Object.entries(dict).reduce((prev, [key, value]) => {
  const newDict = { ...prev };
  // Update prev
  if (newDict[value]) newDict[value].push(key);
  else newDict[value] = [key];
  return newDict;
}, {});

console.log(result);
