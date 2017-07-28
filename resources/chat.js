var message = []
var i = -1

$(document).ready(() => {
  $("#submit").click(checkChat);
  console.log(i)
});

function postSuccess(){
  console.log("successfully o=posted")
}

function checkChat(){
  var dog = $("#chat-area").val();
  if(dog == ""){
    w = 1
  }else{
      addChatMessage(dog);
      message.push(dog);
      $("#chat-area").val('');
      setTimeout(callMe(dog), 20000)
    }
}
function pleaseWork(text){
  setTimeout(callMe, 20000);
}

function callMe(text){
  $.get(window.location, message , getSuccess, "message");

  console.log('');
  if(dog != ""){
    addChatMessage(dog)
  }
}

function BoiWhat(){
  console.log("I was clicked");
}

function getSuccess(){
  console.log("Get successfully")
}

function addChatMessage(text) {
  $('#message-box').append("<fieldset><p>"+text+"</p></fieldset>");
  $.post(window.location, { 'message' : text }, postSuccess, "text");
  i++
}

function append_for_me(){
   history.push('message')
}

//document.write("hey");
//document.write(history[0].message);
