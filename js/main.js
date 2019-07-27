
// $(document).ready(function () {
//     $(".showcolors").click(function () {
      
//       $.ajax({
//         type: "get",
//         dataType: 'json',
//         url: "/allbooks",
  
//         success: function (response,status) {
//           console.log(response);
//         },
//         error: function (msg, status) {
//           console.log("error" + msg + status);
//         },
  
//         complete: function (response, status) {
//           console.log("complete");
  
//         }
//       });
//     });

//   });

  $(document).ready(function () {
      
      $.ajax({
        type: "get",
        dataType: 'json',
        url: "/allbooks",
  
        success: function (response,status) {
        for (let i = 0; i < response.length; i++) {
            console.log(response[i])
            $( "#h11" ).text(response[i]);
          }
        },
        error: function (msg, status) {
          console.log("error" + msg + status);
        },
  
        complete: function (response, status) {
          console.log("complete");
  
        }
      });
    
  });
