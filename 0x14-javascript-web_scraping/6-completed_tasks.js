#!/usr/bin/node
const request = require("request");
const fs = require("fs");

const url = process.argv[2];

request.get({ url }, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const data = JSON.parse(body);

    const completedTasks = data.filter((task) => task.completed);
    const formattedData = completedTasks.reduce((object, task) => {
      const key = task.userId;
      if (!object[key]) return { ...object, [key]: 1 };

      const newObject = { ...object };
      newObject[key]++;
      return newObject;
    }, {});

    console.log(formattedData);
  }
});
