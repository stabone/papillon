
/**
 * Django
 */


var navStatus = $('#navigatorStatus');

// http://diveintohtml5.info/storage.html
// http://html5doctor.com/introducing-web-sql-databases/
// http://code.tutsplus.com/tutorials/working-with-indexeddb--net-34673
// http://www.html5rocks.com/en/mobile/workingoffthegrid/
window.addEventListener("offline", function(e) {
    // check if connection is lost
    navStatus.removeClass();
    navStatus.addClass('navigator-status offline').text('Pazuda savienujus');
}, false);

window.addEventListener("online", function(e) {
    // check if connection is set
    navStatus.removeClass();
    navStatus.addClass('navigator-status online').text('Izsevās pieslēgties');
}, false);

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
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


function populateComments(id) {
    $.ajax({
        type: 'POST',
        dataType: 'json',
        url: '/comment/video/get/comment/',
        data: {
            videoID: id
        },
        headers: {
            'X-CSRFToken': csrftoken
        },
        success: function(data) {
            var commentList = $('#list-'+ id);
            var lastCommentID = $('#list-'+ id +' li').first().data("id");
            if(typeof lastCommentID === 'undefined') {
                lastCommentID = 0;
            }
            // consolepopulateComments.log(lastCommentID);

            commentList.empty();

            $.each(data, function(index, value){
                var comment =
                '<li data-id="'+ value.commentID +'">'+
                    '<div>'+
                        value.comment
                    '</div>'+
                '</li>';
                commentList.prepend(comment);
            });
        },
        error: function(xhr, ajaxOpt, throwError) {
            console.log(xhr.responseText);
        }
    });
}

var loadedVideoComments = new Array();

$('.show-comments').click(function() {
    var videoID = $(this).data('id');
    if(loadedVideoComments.indexOf(videoID) == -1) {
        loadedVideoComments.push(videoID);
        populateComments(videoID);
    }
});

$("#show-red-msg").click(function() {
    $(this).prop('disabled', true);

    // $("#show-unred-msg").prop('disabled', true);
    $(".message-notred").addClass('hide-element');
    console.log("disabled notred messages");
});

$("#show-unred-msg").click(function() {
    $(this).prop('disabled', true);
    // $("#show-red-msg").prop('disabled', true);
    $(".message-red").addClass('hide-element');
    console.log("disabled red messages");
});

$("#show-all-msg").click(function() {
    $("#show-red-msg").prop('disabled', false);
    $("#show-unred-msg").prop('disabled', false);
});

$("#comment-form").submit(function(event) {
    console.log("comment event triggered");

    var commentTag = $('#comment-field');
    var videoID = commentTag.data('video');
    var comment = commentTag.val();

    console.log('video ID: ' + videoID);
    console.log('video comment: ' + comment);

    /*
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
            populateComments(videoID);
        },
        error: function(xhr, ajaxOpt, throwError) {
            // alert(xhr.responseText);
        }
    });
    */

    // return false;
    // event.preventDefault();
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

    // http://nicolasgallagher.com/flexible-css-cover-images/
    return postRating(courseID, starLevel);
});

/* for pomodoro timer */
var timerId;
var classState = true;

$('#timer-icon').hover(function() {
    // show configuration and controls
    $('#timer-tray').toggle().css({'z-index': 999});
});

// $('#timer-start').click(function() {
$('#timer-start').click(function() {
    pomodoroTimer = setInterval('pomodoroEndAlert()', 20000);
    pomodoroIndicatorTimer = setInterval('updateDOM()', 5000);
});

function updateDOM() {
    var timer = $('#timer-icon');
    var timerColor;

    if(classState) {
        timerColor = 'purple time icon';
        classState = false;
    } else {
        timerColor = 'green time icon';
        classState = true;
    }

    timer.attr('class', timerColor);
}


$('.to_trash').click(function() {
    var messageID = $(this).data('id');

    $.ajax({
        type: 'POST',
        dataType: 'json',
        url: '/message/to/trash/',
        data: {
            messageID: messageID,
        },
        headers: {
            'X-CSRFToken': csrftoken
        },
        success: function(data) {
            console.log('all is good');
        },
        error: function(xhr, ajaxOpt, throwError) {
            // alert(xhr.responseText);
        }
    });

    return false;
});


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

function hideElementByID(elemID) {
    $('#'+elemID).hide();
}

var deleteList = {},
    blockList = {};
/** action part*/

$('#delete-info').click(function() {
    if (jQuery.isEmptyObject(deleteList) ) {
        console.log('objekts ir tukšs');
        return ;
    }

    var finalList = Array();

    for(var elem in deleteList) {
        var obj = {};
        /** delete only if is set */
        if (deleteList[elem]) {
            obj.id = elem;

            finalList.push(obj);

            $('<input>').attr({
                type: 'hidden',
                name: 'data',
                value: elem
            }).appendTo('#user-delete-hidden');

        }
    }

    if (finalList.length > 0) {
        $('#user-delete-hidden').submit();
    }

    deleteList = {}
    // sendAction(finalList, '/user/delete/');
});

$('#block-info').click(function() {
    if (jQuery.isEmptyObject(blockList) ) {
        console.log('Empty object');
        return ;
    }

    var finalList = Array();
    for(var key in blockList) {
        var obj = {};
        obj['id']     = key;
        obj['status'] = (blockList[key] === true) ? 1 : 0;
        finalList.push(obj);
    }

    blockList = {};

    if (sendAction(finalList, '/user/block/')) {
        hideRecords(finalList);
    }
});


function sendAction(userObject, postUrl) {
    console.log(userObject);

    $.ajax({
        type: 'POST',
        dataType: 'json',
        url: postUrl,
        data: {
            'data': JSON.stringify(userObject)
        },
        headers: {
            'X-CSRFToken': csrftoken
        },
        success: function(data) {
            // console.log('all is good');
            return true;
        },
        error: function(xhr, ajaxOpt, throwError) {
            console.log(xhr.responseText)
            return false;
        }
    });
}

/** listiners */
$('.delete-user').change(function() {
    var id = $(this).data('id');
    deleteList[id] = this.checked;
});

$('.block-user').change(function() {
    var id = $(this).data('id');
    blockList[id] = this.checked;
});


var correctAnswers = {};
$('.correct-answer').change(function() {
    var questionID = $(this).data('question-id');
    var answerID = $(this).data('answer-id');

    correctAnswers[questionID +'-'+ answerID] = {
                            'question': questionID,
                            'answer': answerID,
                            'status': this.checked
                        };

    console.log(correctAnswers);
});

$('#save-answers').click(function() {
    var answers = Array();

    for (var key in correctAnswers) {
        answers.push({
                question: correctAnswers[key].question,
                answer: correctAnswers[key].answer,
                actioType: (correctAnswers[key].status) ? 1 : 0,
        });

    }

    correctAnswers = {};
    $.ajax({
        type: 'POST',
        dataType: 'json',
        url: '/poll/a/q/correct/',
        data: { 'data': JSON.stringify(answers) },
        headers: { 'X-CSRFToken': csrftoken },
        success: function(data) {
            console.log(data);
        },
        error: function(xhr, ajaxOpt, throwError) {
            console.log(xhr.responseText)
        }
    });
});


tinymce.init({
    selector: 'textarea#wsiwg-editor',
    height: 500,
    toolbar: "insertfile undo redo | styleselect | bold italic | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | link image | print preview media fullpage | forecolor backcolor emoticons",
});

/**
 * AngularJS logic
 *
 **/
var app = angular.module('papillon-app', []);

/*
app.controler('ArticleComment', function($scope, $document, $http) {
    // logic here
    $scope.comment; /// comment for article

    // https://docs.angularjs.org/api/ng/function/angular.element
    var articleID = angular.element($document.querySelector('articleID')).val();

    $http({});

});

*/
