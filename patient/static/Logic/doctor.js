var app = angular.module("validate", []);
app.config(function ($interpolateProvider) {
  $interpolateProvider.startSymbol("{[{");
  $interpolateProvider.endSymbol("}]}");
});
app.controller("formValidator", function ($scope) {
  $scope.show = false;
  $scope.set = function () {
    $scope.show = true;
  };
  $scope.reset = function () {
    $scope.show = false;
  };
  $scope.check = function () {
    console.log("in function");
    if ($scope.show == false) {
      console.log(true);
      return true;
    } else {
      return false;
    }
  };
});
