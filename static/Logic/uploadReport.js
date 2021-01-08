var myApp = angular.module("confirmApp", []);
myApp.config(function ($interpolateProvider) {
  $interpolateProvider.startSymbol("{[{");
  $interpolateProvider.endSymbol("}]}");
});

myApp.controller("confirmthisapp", function ($scope, $http, $interval) {
  $scope.upload = function (a, b, c, d, e) {
    $scope.uploadReport = [];
    $scope.uploadReport.push({
        booking_id:a,
        patient_name:b,
        patient_contact:c,
        Test_name : d,
        Test_date:e
    });
    console.log($scope.uploadReport);

    
  };
});
