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
      var playerValue = document.forms["addForm"]["playerName"].value;
      var ageValue = document.forms["addForm"]["playerAge"].value;
      var nationalityValue = document.forms["addForm"]["nationality"].value;
      var clubValue = document.forms["addForm"]["clubName"].value;
      var ratingValue = document.forms["addForm"]["playerRating"].value;
      var positionValue = document.forms["addForm"]["playerPosition"].value;
      var potentialValue = document.forms["addForm"]["playerPotential"].value;
      // var idValue = document.forms["addForm"]["playerId"].value;

      var letterOnly = /^[a-zA-Z\s]+$/;
      var numberOnly = /^[0-9]+$/;
      var bothlet = /^[0-9a-zA-Z\s]+$/;
      var positionOnly = /^[A-Za-z|\s]+$/;
      // console.log("age value length is : " + ageValue.length);
      console.log("age value is : " + ageValue);

      if (letterOnly.test(playerValue) == false) {
            console.log("player name test is working!!!!!!");
            window.alert('Please input alphabet characters only for player name.');
            document.getElementById('playerName').focus();
            return false;
      }
      if (numberOnly.test(ageValue) == false || ageValue < 1 || ageValue > 99) {
            console.log(" age test is working ");
            console.log("age value is : " + ageValue);
            window.alert('Please input a vaild age between 1 to 99');
            document.getElementById('playerAge').focus();
            return false;
      }
      if (letterOnly.test(nationalityValue) == false) {
            console.log("nationality test is working!!!!!!");
            window.alert('Please input alphabet characters only for nationality.');
            document.getElementById('nationality').focus();
            return false;
      }
      if (bothlet.test(clubValue) == false) {
            console.log("club test is working!!!!!!");
            window.alert('Please input alphabet characters and number only for club name. ');
            document.getElementById('clubName').focus();
            return false;
      }
      if (numberOnly.test(ratingValue) == false || ratingValue < 1 || ratingValue > 99) {
            console.log(" rating test is working ");
            console.log("age value is : " + ratingValue);
            window.alert('Please input a vaild rating between 1 to 99');
            document.getElementById('playerRating').focus();
            return false;
      }
      if (positionOnly.test(positionValue) == false) {
            console.log("position test is working!!!!!!");
            window.alert('Please input alphabet characters only for position and add " | " for multiple positions.');
            document.getElementById('playerPosition').focus();
            return false;
      }
      if (numberOnly.test(potentialValue) == false || potentialValue < 1 || potentialValue > 99) {
            console.log(" potential test is working ");
            console.log("potential value is : " + potentialValue);
            window.alert('Please input a vaild potential rating between 1 to 99');
            document.getElementById('playerPotential').focus();
            return false;
      }
      if (numberOnly.test(idValue) == false) {
            console.log(" id test is working ");
            console.log("id value is : " + idValue);
            window.alert('Please input digit numbers only');
            document.getElementById('playerId').focus();
            return false;
      }


      console.log("hello world");
      return true;

}
