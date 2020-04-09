$(document).ready(function() {

  $('#quote-reshuffle').click(function(){
    var items = _.shuffle($("#quote-tickers").children().toArray());

    $("#quote-tickers").empty();
    
   for(var i = 0; i < items.length; i++){
      $("#quote-tickers").append(items[i]);
    }
   
    console.log(JSON.stringify(items));
  });
});

function commentValidate(){
    var comment = $("#commentsForm").find("textarea[name='comment']").val();

    if (comment.trim().length > 50) {
      return true;
    } else {
      alert("Your comment should have more than 50 characters!");
    }

    return false;
  }

