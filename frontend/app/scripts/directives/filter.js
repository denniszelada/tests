'use strict';
angular.module('frontendApp').
directive('filterManager', function(){
  return {
    restrict: 'E',
    scope:{
      detail: '='
    },
    templateUrl: 'partials/filter-manager.html',
    controller: 'FilterController'
  };
});
