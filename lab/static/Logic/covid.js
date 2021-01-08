var myApp = angular.module("covidInfo", ["ng-fusioncharts"]);
myApp.config(function ($interpolateProvider) {
  $interpolateProvider.startSymbol("{[{");
  $interpolateProvider.endSymbol("}]}");
});

myApp.controller("covidControl", function ($scope, $http) {
  let id = 0;
  let id1 = 0;
  $scope.active = 0;
  $scope.confirmed = 0;
  $scope.recovered = 0;
  $scope.death = 0;
  $scope.indiaShow = true;
  $scope.stateShow = false;
  console.log("world api not working ");

  const url = "https://api.covidindiatracker.com/state_data.json";
  $http.get(url).then(
    (response) => {
      $scope.states = response.data;
    },
    (error) => {
      console.log(error);
    }
  );
  $scope.assign = function (x) {
    id = $scope.id_generator(x);
    $scope.dist = $scope.states[id].districtData;
    $scope.active = $scope.states[id].active;
    $scope.confirmed = $scope.states[id].confirmed;
    $scope.recovered = $scope.states[id].recovered;
    $scope.death = $scope.states[id].deaths;
  };

  $scope.id_generator = function (x) {
    let state = Object.keys($scope.states).length;
    for (let i = 0; i < state; i++) {
      if (x == $scope.states[i].state) {
        id = i;
        break;
      }
    }
    return id;
  };
  $scope.dist_assign = function (x, y) {
    id = $scope.id_generator(x);
    let disLen = Object.keys($scope.states[id].districtData).length;

    for (let i = 0; i < disLen; i++) {
      if (y == $scope.states[id].districtData[i].name) {
        id1 = i;
        console.log(id1);
        break;
      }
    }

    $scope.confirmed = $scope.states[id].districtData[id1].confirmed;
    $scope.active = "-";
    $scope.recovered = "-";
    $scope.death = "-";
  };

  const world_url = "https://api.covid19api.com/summary";
  console.log(world_url);
  $http.get(world_url).then(
    (world_response) => {
      $scope.world = world_response.data;
      console.log($scope.world.Global["TotalConfirmed"]);
      $scope.world_total = $scope.world.Global["TotalConfirmed"];
      $scope.world_recover = $scope.world.Global["TotalRecovered"];
      $scope.world_deaths = $scope.world.Global["TotalDeaths"];

      let worldLen = Object.keys($scope.world.Countries).length;
      for (let i = 0; i < worldLen; i++) {
        if ($scope.world.Countries[i].Country == "India") {
          $scope.india_total = $scope.world.Countries[i].TotalConfirmed;
          console.log(
            "India Total:",
            ($scope.india_total = $scope.world.Countries[i].TotalConfirmed)
          );
          console.log(
            "India Recover:",
            ($scope.india_recover = $scope.world.Countries[i].TotalConfirmed)
          );
          $scope.india_recover = $scope.world.Countries[i].TotalRecovered;
          $scope.india_deaths = $scope.world.Countries[i].TotalDeaths;
          break;
        }
      }
    },
    (world_error) => {
      console.log(world_error);
    }
  );

 // ng show section

 $scope.setShow = function(){
  if($scope.indiaShow == true){
    $scope.indiaShow = false;
    $scope.stateShow = true;
  }
  else{
    $scope.indiaShow = true;
    $scope.stateShow = false;
  }
 };

 

});
