$(document).ready(function () {
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
        if (action === "login") {
          // If login is successful, redirect to chat page
          window.location.href = "/chat";
        } else if (action === "register") {
          // If registration is successful, show a success message and stay on the same page
          alert("Registration successful! You can now log in.");
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
