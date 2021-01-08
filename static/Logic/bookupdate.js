var myApp = angular.module("confirmApp", []);
myApp.config(function ($interpolateProvider) {
  $interpolateProvider.startSymbol("{[{");
  $interpolateProvider.endSymbol("}]}");
});

myApp.controller("confirmthisapp", function ($scope, $http, $interval) {
  
  $scope.labName = "";
  $scope.lab = function (x) {
    $scope.labName = x;
  };
  $scope.data = [];
  $scope.date = [];
  
  console.log($scope.labName);
  $http.get("/labApi").then(
    (api) => {
      let oldLen = Object.keys(api.data).length;
      for (i = 0; i < oldLen; i++) {
        if (
          $scope.labName == api.data[i].lab_id &&
          (api.data[i].bookingStatus == "no" ||
            api.data[i].bookingStatus == "No")
        ) {
          console.log(api.data[i].lab_id);
          $scope.data.push(api.data[i]);
          if ($scope.date.indexOf(api.data[i].test_date) === -1) {
            $scope.date.push(api.data[i].test_date);
          }
        }
      }
      $interval(function () {
        console.log($scope.labName);
        $http.get("/labApi").then(
          (api) => {
            let Len = Object.keys(api.data).length;
            console.log(oldLen);
            if (Len > oldLen) {
              console.log("yes");
              if (
                $scope.labName == api.data[Len -1].lab_id &&
                (api.data[i].bookingStatus == "no" ||
                  api.data[i].bookingStatus == "No")
              ) {
              $scope.data.push(api.data[Len - 1]);
              }
              if ($scope.date.indexOf(api.data[Len -1].test_date) === -1) {
                $scope.date.push(api.data[Len -1].test_date);
              }
            }
            oldLen = Len;
            console.log($scope.data);
          },
          (apierror) => {
            console.log(apierror);
          }
        );
      }, 10000);
    },
    (apierror) => {
      console.log(apierror);
    }
  );
});
