#!/usr/bin/node
const request = require("request");
const util = require("node:util");

const movieId = process.argv[2];
const filmsUrl = "https://swapi-api.alx-tools.com/api/films/" + movieId;
const peopleUrl = "https://swapi-api.alx-tools.com/api/people/";

const requestAsync = util.promisify(request);

(async () => {
  const filmsData = JSON.parse((await requestAsync(filmsUrl)).body);
  const characters = filmsData.characters;
  const peopleData = await getPeopleData();

  const characterNames = characters.map(
    (character) => peopleData.find((person) => person.url === character).name
  );

  characterNames.forEach((name) => {
    console.log(name);
  });
})();

async function getPeopleData() {
  let peopleData = [];
  let next = peopleUrl;

  while (next) {
    const data = JSON.parse((await requestAsync(next)).body);
    peopleData.push(...data.results);
    next = data.next;
  }

  return peopleData;
}
