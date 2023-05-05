$(document).ready(() => {
  $.get("https://swapi-api.alx-tools.com/api/films/?format=json", (data) => {
    const filmsList = data.results.map((film) => $(`<p>${film.title}</p>`));

    filmsList.forEach((film) => {
      $("ul#list_movies").append(film);
    });
  });
});
