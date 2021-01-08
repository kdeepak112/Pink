function checkForm() {
  console.log("inside");
  let gender = document.getElementById('gender').value;
  let user = document.getElementById("username").value;
  let email = document.getElementById("emailid").value;
  let phone = document.getElementById("PhoneNum").value;
  let age = document.getElementById("P_age").value;
  let password = document.getElementById("fPassword").value;
  let r_password = document.getElementById("cPassword").value;

  
  
  
  
  char = [
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "0",
    ";",
    ":",
    "/",
    "?",
    "<",
    ",",
    ">",
    ".",
    "+",
    "-",
    "*",
  ];
  let slen = char.length;
  let ulen = user.length;

  var result = true;

  //gender

  if(gender == ''){
    document.getElementById('gender_check').innerHTML = 'Select Gender';
    result=false;
  }

  if (user == "") {
    document.getElementById("check").innerHTML = "Enter UserName...";
    result = false;
  } else {
    for (var j = 0; j < ulen; j++) {
      for (var k = 0; k < slen; k++) {
        if (user[j] == char[k]) {
          document.getElementById("check").innerHTML =
            "Invalid UserName Entered...";
          result = false;
          break;
        }
      }
    }
  }

  if (email == "") {
    document.getElementById("check1").innerHTML = "Enter Email id";
    result = false;
  }
  var mailformat = "[a-z0-9._%+-]+@[a-z0-9.-]+.[a-z]{2,3}$";

  if (email.match(mailformat)) {
    console.log("match");
  } else {
    document.getElementById("check1").innerHTML = "Invalid Emailid";
    result = false;
  }

  // Phone Number

  if (phone == "") {
    document.getElementById("check2").innerHTML = "Enter Phone Number";
    result = false;
  } else {
    if (phone.length < 10) {
      document.getElementById("check2").innerHTML =
        "Enter 10 digit Phone Number";
      result = false;
    } else {
      let rphone = isNaN(phone);
      if (rphone) {
        document.getElementById("check2").innerHTML =
          "Inavlid Phone Number Entered";
        result = false;
      }
    }
  }

  //Age

  if (age == "") {
    document.getElementById("check4").innerHTML = "Enter Age";
    result = false;
  } else {
    if (age < 18) {
      document.getElementById("check4").innerHTML =
        "You are <b> UNDERAGE </b> my friend...";
      result = false;
    }
  }

  //Password

  let lower = /[a-z]/g;
  let upper = /[A-Z]/g;
  let number = /[0-9]/g;

  if (password.length == "") {
    document.getElementById("check5").innerHTML = "Enter Password";
    result = false;
  } else {
    if (password.length < 8) {
      document.getElementById("check5").innerHTML = "Password must 8 charcters";
      result = false;
    } else {
      if (
        !(
          password.match(lower) &&
          password.match(upper) &&
          password.match(number)
        )
      ) {
        document.getElementById("check5").innerHTML =
          "Password must have: <ul> <li> 8 and more characters long</li> <li> a lower character </li> <li> a upper character </li> <li> a Number </li> </ul>";
        result = false;
      } else {
        if (!(password == r_password)) {
          document.getElementById("check5").innerHTML =
            "Passwords are not same";
          result = false;
        }
      }
    }
  }

  if (result == false) {
    return false;
  } else {
    return true;
  }
}
console.log('angukar')
var myApp = angular.module("lab", []);
myApp.config(function ($interpolateProvider) {
  $interpolateProvider.startSymbol("{[{");
  $interpolateProvider.endSymbol("}]}");
});

myApp.controller("labCon", function ($scope) {
  $scope.gender = ["male", "female"];
});
