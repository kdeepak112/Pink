var myApp = angular.module("selfAssess", []);
myApp.config(function ($interpolateProvider) {
  $interpolateProvider.startSymbol("{[{");
  $interpolateProvider.endSymbol("}]}");
});

myApp.controller("assessControl", function ($scope) {
  
});
