$(document).ready(() => {
  const list = $("ul.my_list");

  $("div#add_item").click(() => {
    list.append($("<li>Item</li>"));
  });

  $("div#remove_item").click(() => {
    list.children().last().remove();
  });

  $("div#clear_list").click(() => {
    list.empty();
  });
});
