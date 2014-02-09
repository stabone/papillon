
$('.ui.dropdown').dropdown({on: 'hover'});

$('.ui.radio.checkbox').checkbox();


function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

function rateTut(tutId) {
    $.ajax({
        type: 'POST',
        url: '/course/tut/rate/',
        data: {'tut_id': tutId},
        headers: {
            'X-CSRFToken': csrftoken
        },
        success: function() {
            // hide rating
            $('tut-rate-' + tutId).hide();
        }
    });

    return false;
}

$('a.rate').click(function(){
    var tutId = parseInt(this.id.split('-')[2]);
    // console.log('cookie for ya: ' + tutId);
    return rateTut(tutId);
});
