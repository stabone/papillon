
$('.ui.dropdown').dropdown({on: 'hover'});

$('.ui.radio.checkbox').checkbox();

$('.ui.checkbox').checkbox({context: false});

$('.ui.selection.dropdown').dropdown();

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
