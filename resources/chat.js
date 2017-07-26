$(document).ready(() =>       {
  setTimeout(checkChat, 30000);
  $("div").click(BoiWhat);
});

function checkChat(){
  $.get(window.location);
  setTimeout(checkChat, 30000);
}

function BoiWhat(){
  console.log("I was clicked");
}
