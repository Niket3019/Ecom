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