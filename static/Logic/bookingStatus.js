history.pushState(null, null, location.href);
history.back();
history.forward();
window.onpopstate = function () {
  history.go(1);
};

var myApp = angular.module("confirmApp", []);
myApp.config(function ($interpolateProvider) {
  $interpolateProvider.startSymbol("{[{");
  $interpolateProvider.endSymbol("}]}");
});

myApp.controller("confirmthisapp", function ($scope, $http, $interval) {
  var someDate = new Date();
  console.log(someDate);
  var mm = someDate.getMonth() + 1;
  $scope.today = someDate.getFullYear() + "-" + mm + "-" + someDate.getDate();
});
