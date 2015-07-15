'use strict';
angular.module('frontendApp').
directive('campaignDescription', function(){
  return {
    restrict: 'E',
    scope:{
      detail: '='
    },
    templateUrl: 'partials/campaign-description.html',
  };
});
