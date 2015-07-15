'use strict';
var today = function(){
  var date = new Date();
  return [date.getDate(), date.getMonth(), date.getFullYear()].join('-');
};

var app = angular.module('frontendApp');
app.controller('FilterController', ['$scope','campaigns',function($scope, campaigns){
  var data = $scope;
  data.date= today();
  data.advisor= '';
  data.advisors = [];
  data.med = '';
  data.media = [];
  data.page = {};

  $scope.setAdvisors = function(response){
    data.advisors = response.data.objects;
    data.page = response.data.meta;
    console.log('yeeeeey!!!' + response.status);
  };

  $scope.setMedia = function(response){
    data.media = response.data.objects;
    data.page = response.data.meta;
    console.log('yeeeeey!!!' + response.status);
  };

  $scope.handleError = function(error){
    data.blah = error.data;
    console.error('Noooo!!! ' + data.blah);
  };

  $scope.createfilters = function(){
    var filter='date='+data.date;
    if(data.advisor !== ''){
      filter = filter + '&advisor='+ data.advisor.advisor;
    }
    return filter;
  };

  $scope.loadAdvisors = function(){
    $scope.filtersUpdated();
    campaigns.fetch('/api/v1/advisors?date='+$scope.date, $scope.setAdvisors, $scope.handleError);
  };

  $scope.loadMedia = function(){
    var filters = $scope.createfilters();
    $scope.filtersUpdated();
    campaigns.fetch('/api/v1/media?'+filters, $scope.setMedia, $scope.handleError);
  };

  $scope.filtersUpdated = function(){
    var filters = $scope.createfilters();
    $scope.$emit('filters-updated',filters);
   };
}]);
