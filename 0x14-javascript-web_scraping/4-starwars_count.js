#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

request.get({ url }, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const data = JSON.parse(body);
    const wedge = 'https://swapi-api.alx-tools.com/api/people/18/';

    const wedgeCount = data.results.reduce((prev, curr) => {
      if (curr.characters.includes(wedge)) {
        return prev + 1;
      } else {
        return prev;
      }
    }, 0);

    console.log(wedgeCount);
  }
});
