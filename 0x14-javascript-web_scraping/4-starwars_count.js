#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

request.get({ url }, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const data = JSON.parse(body);

    const wedgeCount = data.results.reduce((prev, curr) => {
      const wedge = curr.characters.find((value) =>
        value.includes('/people/18')
      );

      if (wedge) {
        return prev + 1;
      } else {
        return prev;
      }
    }, 0);

    console.log(wedgeCount);
  }
});
