$(document).ready(() => {
  $("div#toggle_header").click(() => {
    $("header").toggleClass("red");
    $("header").toggleClass("green");
  });
});
