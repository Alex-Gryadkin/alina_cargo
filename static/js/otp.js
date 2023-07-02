$(document).ready(function(){
    var remainingTime = 59;
    var elem = $('#timer');
    var timer = setInterval(countdown, 1000); //set the countdown to every second
    function countdown() {
      if (remainingTime == -1) {
        clearTimeout(timer);
        $('#timer_div').html('<input class="btn btn-outline-secondary btn-sm" type="submit" value="Отправить код повторно">')
      } else {
        elem.html(remainingTime);
        remainingTime--; //we subtract the second each iteration
      }
    }

});