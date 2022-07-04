
$(window).scroll(function() {
  $.each($('img'), function() {
      if ( $(this).attr('data-src') && $(this).offset().top < ($(window).scrollTop() + $(window).height() + 100) ) {
          var source = $(this).data('src');
          $(this).attr('src', source);
          $(this).removeAttr('data-src');
      }
  })
})

function getCookie(name){
    var cookieValue = null;

    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();

            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
};

(function($) {
    $('#lazyLoadLink').on('click', function() {
      var link = $(this);
      var page = link.data('page');

      var csrf_token = getCookie('csrftoken');
      
      $.ajax({
        type: 'post',
        url: '/lazy_load_posts/',
        data: {
          'page': page,
          'csrfmiddlewaretoken': csrf_token
        },
        success: function(data) {
          // if there are still more pages to load,
          // add 1 to the "Load More Posts" link's page data attribute
          // else hide the link
          if (data.has_next) {
              link.data('page', page+1);
          } else {
            link.hide();
          }
          // append html to the posts div
          $('#posts').append(data.posts_html);
        },
        error: function(xhr, status, error) {
          // shit happens friends!
        }
      });
    });
  }(jQuery));
