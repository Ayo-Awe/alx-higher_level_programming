#!/usr/bin/node

function addMeMaybe (x, theFunction) {
  theFunction(x + 1);
}

module.exports = { addMeMaybe };
