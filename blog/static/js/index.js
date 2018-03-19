let posts = $('.js-post');

posts.mouseover(
  function (e) {
    $(e.target).tooltip('show');
  }
);

posts.mouseout(
  function (e) {
    $(e.target).tooltip('hide');
  }
);