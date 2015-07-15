'use strict';
var app = angular.module('frontendApp');
app.controller('FilterController', ['$scope','campaigns',function($scope, campaigns){
  var data = $scope;
  data.date= '';
  data.advisor= '';
  data.advisors = [''];
  data.med = '';
  data.media = [''];
  data.page = {};

  $scope.setAdvisors = function(response){
    data.advisors = data.advisors.concat(response.data.objects);
    data.page = response.data.meta;
    console.log('yeeeeey!!!' + response.status);
  };

  $scope.setMedia = function(response){
    data.media = data.media.concat(response.data.objects);
    data.page = response.data.meta;
    console.log('yeeeeey!!!' + response.status);
  };

  $scope.handleError = function(error){
    data.blah = error.data;
    console.error('Noooo!!! ' + data.blah);
  };

  $scope.createfilters = function(){
    var filter='';
    if((data.date!=='')){
      filter = filter + 'date='+data.date;
    }
    if(data.advisor !== ''){
      filter = filter + '&advisor='+ data.advisor.advisor;
    }
    if(data.med !== ''){
      filter = filter + '&media='+data.med.media;
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

  $scope.cleanData = function(filterLevel){
    switch(filterLevel){
      case 3:
        data.cleanMedia();
        break;
      case 2:
        data.cleanAdvisors();
        break;
      case 1:
        data.cleanDate();
        break;
    }
    data.filtersUpdated();
  };

  $scope.cleanAll = function(){
    data.cleanMedia(false);
    data.cleanAdvisors(false);
    data.cleanDate(false);
    data.filtersUpdated(false);
  };

  $scope.cleanDate = function(partial){
    partial = partial !== false;
    data.date= '';
    if(partial){
      data.filtersUpdated();
    }
  };

  $scope.cleanAdvisors = function(partial){
    partial = partial !== false;
    data.advisor= '';

    if(partial){
      data.cleanMedia(false);
      data.filtersUpdated();
    }
    else{
      data.advisors = [''];
    }
  };

  $scope.cleanMedia = function(partial){
    partial = partial !== false;
    data.med = '';
    if(!partial){
      data.media = [''];
    }
    data.filtersUpdated();
  };
}]);
