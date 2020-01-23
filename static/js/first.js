console.log("first");

function countSelectedImages() {
  return $(".selected").length;
}

$(function() {
  // Initialize
  $("#info").hide();
  $("#submit").prop("disabled", true);

  // Events
  $("img").on("click", function() {
    $(this).toggleClass("selected border-solid border-4 border-red-600");
    if (0 < countSelectedImages() && countSelectedImages() <= 10) {
      $("#submit").prop("disabled", false);
      $("#submit").addClass("bg-red-500 border-red-700 hover:bg-red-700");
      $("#submit").removeClass("bg-gray-500 border-gray-700 hover:bg-gray-700");
    } else {
      $("#submit").prop("disabled", true);
      $("#submit").addClass("bg-gray-500 border-gray-700 hover:bg-gray-700");
      $("#submit").removeClass("bg-red-500 border-red-700 hover:bg-red-700");
    }
  });

  // Submit
  $("#submit").on("click", function() {
    let images = [];
    $(".selected").each(function() {
      images.push($(this).attr("alt"));
    });
    $("#submit").prop("disabled", true);
    $("#submit").addClass("bg-gray-500 border-gray-700 hover:bg-gray-700");
    $("#submit").removeClass("bg-red-500 border-red-700 hover:bg-red-700");
    $.ajax({
      url: "/move",
      type: "POST",
      data: {
        images: images
      },
      dataType: "json",
      success: function(data, dataType) {
        console.log("Success!");
        console.log(data);
        $("#info").fadeIn("slow", function() {
          setTimeout(location.reload(), 15000);
        });
      },
      error: function(XMLHttpRequest, textStatus, errorThrown) {
        console.log("Error!");
        console.log(textStatus);
        console.log(errorThrown);
      },
      complete: function(XMLHttpRequest, textStatus) {
        console.log("Complete!");
        console.log(XMLHttpRequest);
      }
    });
    return false;
  });
});
