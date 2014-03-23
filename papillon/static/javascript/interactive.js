
/**
 * Django
 */

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

$("#comment-form").submit(function(event) {
    console.log("comment event triggered");

    var commentTag = $('#comment-field');
    var videoID = commentTag.data('video');
    var comment = commentTag.val();

    console.log('video ID: ' + videoID);
    console.log('video comment: ' + comment);

    $.ajax({
        type: 'POST',
        dataType: 'json',
        url: '/comment/video/add/comment/',
        data: {
            videoID: videoID,
            comment: comment,
        },
        headers: {
            'X-CSRFToken': csrftoken
        },
        success: function(data) {
            // alert(data.success);
        },
        error: function(xhr, ajaxOpt, throwError) {
            // alert(xhr.responseText);
        }
    });

    return false;
    // event.preventDefault();
    // event.stopPropagation();
});

function postRating(courseID, starLevel) {
    $.ajax({
        type: 'POST',
        dataType: 'json',
        url: '/course/tut/rate/',
        data: {
            'tut_id': courseID,
            'level': starLevel
        },
        headers: {
            'X-CSRFToken': csrftoken
        },
        success: function(data) {
            var ratingStatus;
            if(typeof data.error !== 'undefined') {
                ratingStatus =
                        '<div class="ui error message">'+
                            '<i class="close icon"></i>'+
                            '<p>'+ data.error +'</p>'+
                        '</div>';
            }
            if(typeof data.rated !== 'undefined') {
                ratingStatus = '<div>'+ data.rated +'</div>';
            }
            $('#course-' + courseID).prepend(ratingStatus);
        }
    });

    return false;
}

$('.rating').click(function(){
    var starLevel = $(this).data('star');
    var courseID = $(this).data('course');

    return postRating(courseID, starLevel);
});

/* for pomodoro timer */
var timerId;
var classState = true;

$('#timer').click(function() {
    startPomodoro();
});

function startPomodoro() {
    timerID = setInterval('pomodoro()', 1000);
}

function pomodoro() {
    updateDOM();
}

function updateDOM() {
    console.log(" it's on going process");
    var timer = $('#timer');
    var purple = 'purple time icon';
    var green = 'green time icon';
    var timerColor;

    if(classState) {
        timerColor = purple;
        classState = false;
    } else {
        timerColor = green;
        classState = true;
    }

    timer.attr('class', timerColor);
}

function stopPomodoro() {
    console.log(" timer END");
    clearTimeout(timerId);
}


/**
 * Semantic UI
 */
$('.ui.dropdown').dropdown({on: 'hover'});

$('.ui.radio.checkbox').checkbox();

$('.ui.checkbox').checkbox({context: false});

$('.ui.selection.dropdown').dropdown();

/**
 * document for forcing selection
 */
$(document).on('click', '.ui.error.message', function() {
    $(this).closest('.message').fadeOut();
});


