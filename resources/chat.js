var message = []
var i = -1

$(document).ready(() => {
  $("#submit").click(checkChat);
  pleaseWork()
  console.log(i)
});

function postSuccess(){
  console.log("successfully o=posted")
}

function checkChat(){
  var dog = $("#chat-area").val();
  if(dog == ""){
    w=1
  }else{
      addChatMessage(dog);
      message.push(dog);
      $.post(window.location, { 'message' : dog }, postSuccess, "text");
      $("#chat-area").val('');
      setTimeout(callMe(dog), 30000)
    }
}
function pleaseWork(text){
  setTimeout(callMe, 30000);
}

function callMe(text){
  var result = $.post(window.location, {'message': text}, getSuccess, "message");
  setTimeout(callMe, 30000);
  if(result != ""){
    addChatMessage(result)
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
}

function append_for_me(){
   history.push('message')
}

//document.write("hey");
//document.write(history[0].message);
