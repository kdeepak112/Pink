function updateForm() {
  console.log("inside update");

  let user = document.getElementById("username").value;
  let email = document.getElementById("emailid").value;
  let phone = document.getElementById("PhoneNum").value;
  let age = document.getElementById("P_age").value;
  console.log(age);
  let Oldpassword = document.getElementById("OldPassword").value;

  let NewPassword = document.getElementById("NewPassword").value;
  console.log(NewPassword);
  let cPassword = document.getElementById("cPassword").value;

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

  var mailformat = "[a-z0-9._%+-]+@[a-z0-9.-]+.[a-z]{2,3}$";

  if (email.match(mailformat)) {
    console.log("match");
  } else {
    document.getElementById("check1").innerHTML = "Invalid Emailid";
    result = false;
  }

  // Phone Number

  if (phone.length < 10) {
    document.getElementById("check2").innerHTML = "Enter 10 digit Phone Number";
    result = false;
  } else {
    let rphone = isNaN(phone);
    if (rphone) {
      document.getElementById("check2").innerHTML =
        "Inavlid Phone Number Entered";
      result = false;
    }
  }

  //Age

  if (age < 18) {
    document.getElementById("check4").innerHTML =
      "You are <b> UNDERAGE </b> my friend...";
    result = false;
  }

  //Password

  let lower = /[a-z]/g;
  let upper = /[A-Z]/g;
  let number = /[0-9]/g;

  if (Oldpassword == "") {
    document.getElementById("check5").innerHTML = "Enter Password";
    result = false;
  }
  if (NewPassword == "") {
    
    
  } else {
    if (NewPassword.length < 8) {
      document.getElementById("check6").innerHTML = "Password must 8 charcters";
      result = false;
    } else {
      if (
        !(
          NewPassword.match(lower) &&
          NewPassword.match(upper) &&
          NewPassword.match(number)
        )
      ) {
        document.getElementById("check5").innerHTML =
          "Password must have: <ul> <li> 8 and more characters long</li> <li> a lower character </li> <li> a upper character </li> <li> a Number </li> </ul>";
        result = false;
      } else {
        if (!(NewPassword == cPassword)) {
          document.getElementById("check5").innerHTML =
            "Passwords are not same";
          result = false;
        }
      }
    }
  }
  console.log(result)
  return result;
}
