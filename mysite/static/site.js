
// const form = document.getElementById('form');
// const playerName_input = document.getElementById('playerName').value;

// form.addEventListener('submit', e => {
// 	e.preventDefault();
//
// 	checkValid();
// });
// function returnToPreviousPage() {
//     window.history.back();
// }

function checkValid() {
      // e.preventDefault();
      // var playerName_input = document.getElementById('playerName').value;
      var x = document.forms["addForm"]["playerName"].value;
      var letterOnly = /^[a-zA-Z]+$/;
      var numberonly = /^[0-9]+$/;
      var bothNumLet = /^[0-9a-zA-Z]+$/;
      var positionOnly = /^[A-Za-z]+$/;

      // if (playerName_input == letterOnly){
      // if (playerName_input.match(letterOnly)) {
      if (letterOnly.test(x) == false) {
            console.log("here!!!!!!");
            window.alert('Please input only alphabet characters only.');
            document.getElementById('playerName').focus();
            // e.preventDefault();
            return false;
      }
      // alert('Your name have accepted : you can try another')
      console.log("hello world");
      return true;
}
//
// $(function() {
//       $('#form').on('submit', function(event) {
//             if (!isValid()) {
//                  event.preventDefault();
//             }
//
//       })
// })

      // alert('Please input only alphabet characters only.');
      // playerName_input.focus();
      //       return false;

