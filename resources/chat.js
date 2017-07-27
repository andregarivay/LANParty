var message = []

$(document).ready(() => {
  $("#submit").click(checkChat);

});

function checkChat(){
  var dog = $("#chat-area").val();
  if(dog == ""){
    i=1
  }else{
      addChatMessage(dog);
      $("#chat-area").val('');
      //$("fieldset").post(window.location, message,   )
    }
}
function pleaseWork(){
  setTimeout()

}

function callMe(text){
  $("fieldset").get(window.location, x)
}
function BoiWhat(){
  console.log("I was clicked");
}

function addChatMessage(text) {
  $('#message-box').append("<fieldset><p>"+text+"</p></fieldset");
}

function append_for_me(){
   history.push('message')
}

//document.write("hey");
//document.write(history[0].message);
