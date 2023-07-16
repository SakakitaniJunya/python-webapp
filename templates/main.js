$(document).ready(function () {
  // When the submit button is clicked, check which radio button is selected and send the appropriate request to the server
  $("#submitAction").click(function () {
    var email = $("#email").val();
    var password = $("#password").val();
    var action = $('input[name="action"]:checked').val();
    var url = "/" + action;

    $.ajax({
      url: url,
      type: "POST",
      data: { email: email, password: password },
      success: function (response) {
        alert(response.message);
        if (action == "login") {
          windows.location.href = "/chat";
        } else if (action == "registor") {
          alert("Registor");
        }
      },
      error: function (error) {
        alert(error.responseText || error.responseJSON.message);
      },
    });

    // Clear the input fields
    $("#email").val("");
    $("#password").val("");

    return false;
  });
});

