function checkDoc() {
  console.log("In the function");
  let user = document.getElementById("username").value;
  let email = document.getElementById("emailid").value;
  let phone = document.getElementById("PhoneNum").value;

  let password = document.getElementById("fPassword").value;
  let r_password = document.getElementById("cPassword").value;
  let experience = document.getElementById("Experience").value;

  let specialisation = document.getElementById("specialisation").value;
  let gender = document.getElementById("gender").value;
  let age = document.getElementById("age").value;

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

  if(gender == '' || specialisation == ''){
    document.getElementById("check_special").innerHTML = "Select Gender and Specialization";
    result=false;
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

  //Age

  if(age == ''){
    document.getElementById("checkage").innerHTML = "Enter Age";
    result = false;
  }else{
    if(age < 34){
      result = false;
      document.getElementById("checkage").innerHTML = "Age not allowed";
    }
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

  // Address

  //experience

  if (experience < 10 || experience == "" || experience > age) {
    document.getElementById("check6").innerHTML = "experience is Invalid";
    result = false;
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

var myApp = angular.module("labInfo", []);
myApp.config(function ($interpolateProvider) {
  $interpolateProvider.startSymbol("{[{");
  $interpolateProvider.endSymbol("}]}");
});

myApp.controller("labControl", function ($scope, $http) {
  $scope.specialisation = [
    "General Physician",
    "Pediatrician",
    "Orthopedician",
    "Gynecologist",
    "Gastroenterologist",
    "Dietician",
  ];
  $scope.gender = ["male", "female"];
});

myApp.controller("formValidator", function ($scope) {});
