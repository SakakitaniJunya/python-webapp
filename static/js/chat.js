function createMessageElement(email, message, timestamp, isCurrentUser) {
  var alignment = isCurrentUser ? "flex justify-end" : "flex justify-start";
  var bgColor = isCurrentUser ? "bg-green-100" : "bg-white";

  var messageElement = $("<div>")
    .addClass(`border rounded-lg p-3 mb-2 ${alignment} ${bgColor}`)
    .append(
      $("<div>")
        .addClass("w-full")
        .append(
          $("<img>")
            .text(email ? email : "None")
            .addClass("block text-indigo-600"),
          $("<strong>")
            .text(email ? email : "None")
            .addClass("block text-indigo-600"),
          $("<p>").text(message).addClass("mb-1"),
          $("<span>").text(timestamp).addClass("text-xs text-gray-600")
        )
    );

  return messageElement;
}

function getMessages() {
  $.getJSON("/get_messages", function (data) {
    $("#message-container").empty();

    var userMessages = data.userMessageList;
    var allMessages = data.allMessagesList;
    allMessages.forEach(function (message) {
      var isCurrentUser = userMessages.some(function (userMessage) {
        return userMessage.MESSAGE_ID === message.MESSAGE_ID;
      });

      var messageElement = createMessageElement(
        message.EMAIL,
        message.MESSAGE,
        message.CREATE_AT,
        isCurrentUser
      );
      $("#message-container").append(messageElement);
    });
  });
}

// Make sure to call getMessages when the page loads

$(document).ready(function () {
  getMessages(); // Call once immediately upon page load

  // Then call every 5 seconds
  setInterval(getMessages, 5000);
});

$(function () {
  $("#send-button").click(function () {
    var message = $("#message-input").val();
    //var userId = getCurrentUserId();

    $.ajax({
      url: "/chat",
      type: "POST",
      contentType: "application/json", // Content-Type を 'application/json' に設定
      data: JSON.stringify({ message: message }), // JSON 文字列に変換
      success: function (response) {},
      error: function (error) {
        alert(error.responseText || error.responseJSON.message);
      },
    });
  });
});
