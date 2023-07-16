$(document).ready(function () {
  var socket = io.connect("https://" + document.domain + ":" + location.port);

  // When the submit button is clicked, check which radio button is selected and send the appropriate request to the server
  $("#send-button").click(function () {
    var message = $("#message-input").val();
    alert("hoge");
    // Perform some basic input validation
    if (message.length === 0) {
      alert("Message cannot be empty");
      return false;
    }

    socket.emit("message", {
      user_id: "currentUser",
      message: message,
      timestamp: new Date().toISOString(),
    });

    $("#message-input").val("");
    return false;
  });

  socket.on("message", function (data) {
    var messageElement;
    if (data.user_id === "currentUser") {
      messageElement = createMessageElement(
        avatarURL,
        data.user_id,
        data.message,
        data.timestamp,
        true
      );
    } else {
      messageElement = createMessageElement(
        avatarURL,
        data.user_id,
        data.message,
        data.timestamp,
        false
      );
    }
    $("#message-container").append(messageElement);
  });
});
