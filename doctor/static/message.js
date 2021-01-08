var myApp = angular.module("confirmApp", []);
myApp.config(function ($interpolateProvider) {
  $interpolateProvider.startSymbol("{[{");
  $interpolateProvider.endSymbol("}]}");
});

myApp.controller("confirmthisapp", function ($scope, $http, $interval,$timeout) {
  
  $timeout(function(){ $("#messageDiv").scrollTop($("#messageDiv")[0].scrollHeight);}, 1000);
  $scope.PName = "";
  $scope.DName = "";
  $scope.lab = function (x, y) {
    $scope.PName = x;
    $scope.DName = y;
  };
  $scope.messages = [];
  $scope.docmssg = [];
  $http.get("/MessageApi").then(
    (api) => {
      console.log(api.data);
      let oldLen = Object.keys(api.data).length;
      for (i = 0; i < oldLen; i++) {
        if (
          $scope.PName == api.data[i].from_patient &&
          $scope.DName == api.data[i].to_doctor 
        ) {
          console.log(api.data[i].from_patient, api.data[i].to_doctor);
          $scope.messages.push({
            message: api.data[i].message,
            timestamp: api.data[i].timestamp,
          });
          
        }
      }
      $interval(function () {
        console.log("patient");
        $http.get("/MessageApi").then(
          (api) => {
            let Len = Object.keys(api.data).length;
            console.log(oldLen);
            if (Len > oldLen) {
              console.log("yes");
              if (
                $scope.PName == api.data[Len - 1].from_patient &&
                $scope.DName == api.data[Len - 1].to_doctor 
              ) {
                $scope.messages.push({
                  message: api.data[Len - 1].message,
                  timestamp: api.data[Len - 1].timestamp,
                });
                $timeout(function(){ $("#messageDiv").scrollTop($("#messageDiv")[0].scrollHeight);});
              }
            }
            oldLen = Len;
          },
          (apierror) => {
            console.log(apierror);
          }
        );
      }, 1000);
    },
    (apierror) => {
      console.log(apierror);
    }
  );
});
