'use strict';
var app = angular.module('frontendApp');
app.controller('CampaignController',['$scope',function($scope){
  $scope.firstBanner= function(){
    var banners = $scope.detail.banners;
    for(var banner in banners){
      if(/\.(png|jpg|jpeg|gif)$/i.test(banners[banner]))
      {
        return banners[banner];
      }
    }
    return 'images/campaign.png';
  };
}]);
