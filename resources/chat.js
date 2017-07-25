$(document).ready(){
  setTimeout(checkChat, 60000);
  $("div").click(BoiWhat);
}

function checkChat(){
  $.get(window.location);
  setTimeout(checkChat, 60000);
}

function BoiWhat(){
  $("div").css("background-color", "#FFFF9C").animate({ backgroundColor: "#FFFFFF"}, 1500);
}
