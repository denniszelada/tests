'use strict';
angular.module('frontendApp').
directive('chart', function(){
  return {
    restrict: 'E',
    templateUrl: 'partials/chart.html',
    controller: 'ChartController',
    controllerAs: 'chart'
  };
});
