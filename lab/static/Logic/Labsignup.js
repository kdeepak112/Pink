function checkForm() {
  console.log("In the function");
  let user = document.getElementById("username").value;
  let email = document.getElementById("emailid").value;
  let phone = document.getElementById("PhoneNum").value;
  let address = document.getElementById("Labaddress").value;
  let password = document.getElementById("fPassword").value;
  let r_password = document.getElementById("cPassword").value;
  let pincode = document.getElementById("pincode").value;
  let state = document.getElementById("state").value;
  let district = document.getElementById("district").value;

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
    "*",
  ];
  let slen = char.length;
  let ulen = user.length;

  var result = true;

  if (state == "") {
    result = false;
  }

  if (district == "") {
    console.log("district");
    document.getElementById("state_check").innerHTML = "Select city and suburb";
    result = false;
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
      console.log("nan");
      if (rphone) {
        document.getElementById("check2").innerHTML =
          "Inavlid Phone Number Entered";
        result = false;
      } else {
        if (Number(phone) < 1) {
          document.getElementById("check2").innerHTML =
            "Inavlid Phone Number Entered";
          console.log(0000);
          result = false;
        }
      }
    }
  }

  // Address

  if (address == "") {
    document.getElementById("check3").innerHTML = "Address cant be left empty.";
    result = false;
  }

  //Pincode

  if ((pincode < 6 && pincode > 6) || pincode == "") {
    document.getElementById("check6").innerHTML = "Pincode is Invalid";
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
  $scope.labStates = [
    {
      city: "mumbai",
      suburb: ["Ghatkopar", "colaba", "dadar"],
    },
    {
      city: "pune",
      suburb: ["pimpri", "Lonavala", "Shivajinagar"],
    },
  ];

  $scope.assign = function (x) {
    console.log(x);
    city = x;
    for (var i = 0; i < $scope.labStates.length; i++) {
      if ($scope.labStates[i].city == x) {
        $scope.dist = $scope.labStates[i].suburb;
      }
    }
  };
});

myApp.controller("formValidator", function ($scope) {});
