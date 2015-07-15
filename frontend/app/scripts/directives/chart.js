'use strict';
angular.module('frontendApp').
directive('chart', function(){
  return {
    restrict: 'E',
    scope:{
      detail: '='
    },
    templateUrl: 'partials/chart.html',
  };
});
