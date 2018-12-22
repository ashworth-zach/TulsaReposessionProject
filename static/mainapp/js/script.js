$('.ajax_form').submit(function (e) {
    e.preventDefault()
})
$('#ajax_tag').keyup(function () {
    console.log('Sending Ajax request to /find')
    console.log('Submitting the following data', $(this).parent().serialize())
    $.ajax({
        url: '/find',
        /* Where should this go? */
        method: 'post',
        /* Which HTTP verb? */
        data: $(this).parent().serialize(),
        /* Any data to send along? */
        success: function (serverResponse) { /* What code should we run when the server responds? */
            $('#mytable').html(serverResponse)
        }
    })
});
var table = '#mytable'
$('#maxRows').on('change', function () {
    $('.pagination').html('')
    var trnum = 0
    var maxRows = parseInt($(this).val())
    var totalRows = $(table + ' tbody tr').length
    $(table + ' tr:gt(0)').each(function () {
        trnum++
        if (trnum > maxRows) {
            $(this).hide()
        }
        if (trnum <= maxRows) {
            $(this).show()
        }
    })
    if (totalRows > maxRows) {
        var pagenum = Math.ceil(totalRows / maxRows)
        for (var i = 1; i <= pagenum;) {
            $('.pagination').append('<li data-page="' + i + '">\<span>' + i++ + '<span class="sr-only">(current)</span>|</span>\</li>').show()
        }
    }
    $('.pagination li:first-child').addClass('active')
    $('.pagination li').on('click', function () {
        var pageNum = $(this).attr('data-page')
        var trIndex = 0;
        $('.pagination li').removeClass('active')
        $(this).addClass('active')
        $(table + ' tr:gt(0)').each(function () {
            trIndex++
            if (trIndex > (maxRows * pageNum) || trIndex <= ((maxRows * pageNum) - maxRows)) {
                $(this).hide()
            } else {
                $(this).show()
            }
        })
    })
})
$(function () {
    $('table tr:eq(0)').prepend('<th>ID</th>')
    var id = 0;
    $('table tr:gt(0)').each(function () {
        id++
        $(this).prepend('<td>' + id + '</td>')
    })
})
navigator.getUserMedia = (navigator.getUserMedia ||
    navigator.webkitGetUserMedia ||
    navigator.mozGetUserMedia ||
    navigator.msGetUserMedia);

var video;
var webcamStream;
var x;
function startWebcam() {
    if (navigator.getUserMedia) {
        navigator.getUserMedia(

            // constraints
            {
                video: true,
                audio: false
            },

            // successCallback
            function (localMediaStream) {
                video = document.querySelector('video');
                video.src = window.URL.createObjectURL(localMediaStream);
                webcamStream = localMediaStream;
            },

            // errorCallback
            function (err) {
                console.log("The following error occured: " + err);
            }
        );
    } else {
        console.log("getUserMedia not supported");
    }
}

function stopWebcam() {
    webcamStream.stop();
}
//---------------------
// TAKE A SNAPSHOT CODE
//---------------------
var canvas, ctx;

function init() {
    // Get the canvas and obtain a context for
    // drawing in it
    canvas = document.getElementById("myCanvas");
    ctx = canvas.getContext('2d');
}

function snapshot() {
    // Draws current image from the video element into the canvas
    ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
}
function upload() {
    var result = $('#myCanvas')[0].toDataURL();
    var strImage = result.replace(/^data:image\/[a-z]+;base64,/, "");
    $('#canvasdata')[0].value = strImage
}
