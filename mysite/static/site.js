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

      var letterOnly = /^[a-zA-Z\s]+$/;
      var numberOnly = /^[0-9]+$/;
      var bothlet = /^[0-9a-zA-Z\s]+$/;
      var positionOnly = /^[A-Za-z|\s]+$/;

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
            window.alert('Please input a valid position and add " | " for multiple positions without spaces');
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

      console.log("hello world");
      return true;

}

function searchValid() {
      var letterOnly = /^[a-zA-Z\s]+$/;
      var numberOnly = /^[0-9]+$/;
      var bothlet = /^[0-9a-zA-Z\s]+$/;
      var positionOnly = /^[A-Za-z|\s]+$/;

      // var checkDropdown = document.getElementById("dropdown").value;
      var checkDropdown = document.forms["searchForm"]["dropdown"].value;
      // var dropdown1 = checkDropdown.options[checkDropdown.player_name].value;
      var inputValue = document.forms["searchForm"]["name"].value;
      if (checkDropdown == "player_name" && letterOnly.test(inputValue) == false) {
            // letterOnly.test(inputValue) == false
            console.log("player name test is working!!!!!!");
            window.alert('Please input alphabet characters only for player name.');
            // document.getElementById('playerName').focus();
            return false;
      }

      if (checkDropdown == "age" && (numberOnly.test(inputValue) == false || inputValue < 1 || inputValue > 99)) {
            console.log(" age test is working ");
            console.log("age value is : " + inputValue);
            window.alert('Please input a vaild age between 1 to 99');
            // document.getElementById('playerAge').focus();
            return false;
      }

      if (checkDropdown == "nationality" && letterOnly.test(inputValue) == false) {
            // letterOnly.test(inputValue) == false
            console.log("nationality test is working!!!!!!");
            window.alert('Please input alphabet characters only for nationality.');
            // document.getElementById('playerName').focus();
            return false;
      }

      if (checkDropdown == "club" && bothlet.test(inputValue) == false) {
            console.log("club test is working!!!!!!");
            window.alert('Please input alphabet characters and number only for club name. ');
            // document.getElementById('clubName').focus();
            return false;
      }

      if (checkDropdown == "rating" && (numberOnly.test(inputValue) == false || inputValue < 1 || inputValue > 99)) {
            console.log(" rating test is working ");
            console.log("rating value is : " + inputValue);
            window.alert('Please input a vaild rating between 1 to 99');
            // document.getElementById('playerAge').focus();
            return false;
      }

      if (checkDropdown == "position" && positionOnly.test(inputValue) == false) {
            // letterOnly.test(inputValue) == false
            console.log("position test is working!!!!!!");
            window.alert('Please input a valid position and add " | " for multiple positions without spaces');
            // document.getElementById('playerName').focus();
            return false;
      }


      console.log("hello world");
      return true;
}

$(document).ready(function () {
      // $("#lowRated").hide();
      $('#btnToggle').on('click', function () {
            $("#topRated").toggle();
            // $("#lowRated").toggle('#topRated');
      });
});
// $("#btnToggle").on('click', function () {
//       $("#topRated").toggle();
//       $("#lowRated").toggle();
// });

