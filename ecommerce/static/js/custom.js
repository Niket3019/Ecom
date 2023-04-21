// to get current year
function getYear() {
    var currentDate = new Date();
    var currentYear = currentDate.getFullYear();
    document.querySelector("#displayYear").innerHTML = currentYear;
}

getYear();
$(document).ready(function(){
    $(".box").slice(0, 6).fadeIn()
    $(".btn_box").click(function(){
      $(".box").slice(0, 18).fadeIn();
      $(this).fadeOut();
    })
  })
  const video = document.getElementById('my-video'); // Replace "myVideo" with the ID of your video element
  let startTime = 0; // Initialize a variable to store the start time
  let pauseTime = 0; // Initialize a variable to store the pause time
  
  // Add a loadedmetadata event listener to the video element
  video.addEventListener('loadedmetadata', () => {
    console.log('Video duration:', video.duration, 'seconds');
  });
  
  // Add a timeupdate event listener to the video element
  video.addEventListener('timeupdate', () => {
    if (video.paused) {
      // The video is currently paused
      pauseTime = video.currentTime;
    } else {
      // The video is currently playing
      if (startTime === 0) {
        // The video has just started playing
        startTime = video.currentTime;
      }
    }
  });
  
  // Add a pause event listener to the video element
  video.addEventListener('pause', () => {
    const duration = pauseTime - startTime;
    console.log('Video paused at:', duration, 'seconds');
  
    // Send the start and pause times of the video to the Django view using AJAX
    const data = { start_time: startTime, pause_time: pauseTime, duration: duration,total_duration:video.duration};
    $.ajax({
      url: '',
      type: 'POST',
      data: JSON.stringify(data),
      contentType: 'application/json; charset=utf-8',
      dataType: 'json',
      
      success: function(response) {
        console.log('Response:', response);
      },
      error: function(error) {
        console.error('Error:', error);
      }
    });
  });
  
  
  
  
  
    $(document).ready(function() {

    var buttonClicks = {};
    $('#button-hide,#button-2,#button-3,#button-4,#button-5').on('click', function() {
      var buttonId = $(this).text();
      if (!buttonClicks[buttonId]) {
        buttonClicks[buttonId] = 0;
      }
      buttonClicks[buttonId]++;
      console.log('Button ' + buttonId + ' clicks: ' + buttonClicks[buttonId]);
  
      // Send AJAX request to save the button click count
      $.ajax({
        type: 'POST',
        url: '',
        data: {
          'button_id': buttonId,
          'count': buttonClicks[buttonId],

        },
        success: function(response) {
          console.log('Button click count saved successfully.');
        },
        error: function(xhr, status, error) {
          console.log('Error saving button click count: ' + error+status+xhr);
        }
      });
    });
  });