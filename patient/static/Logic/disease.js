var myApp = angular.module("myApp", []);
myApp.config(function ($interpolateProvider) {
  $interpolateProvider.startSymbol("{[{");
  $interpolateProvider.endSymbol("}]}");
});

myApp.controller("thisapp", function ($scope, $http) {
  $http.get("/diseaseApi").then(
    (api) => {
      console.log(api.data);
      $scope.data = api.data;
      console.log($scope.data);
    },
    (apierror) => {
      console.log(apierror);
    }
  );

  $scope.specific = {};
  console.log("Hello", $scope.specific);
  $scope.assign = function (que) {
    console.log("Inside functiion");
    $scope.specific = que;
    console.log($scope.specific);
  };
});
