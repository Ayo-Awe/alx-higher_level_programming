$(document).ready(() => {
  $.get("https://fourtonfish.com/hellosalut/?lang=fr", (data) => {
    console.log(data);
    $("div#hello").text(data.hello);
  });
});
