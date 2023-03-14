#!/usr/bin/node

exports.esrever = function (list = []) {
  const reversed = [];
  while (list.length > 0) {
    // pop last element and add to reversed list
    const head = list.pop();
    reversed.push(head);
  }
  return reversed;
};
