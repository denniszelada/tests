'use strict';

/**
 * @ngdoc function
 * @name frontendApp.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of the frontendApp
 */
angular.module('frontendApp')
  .controller('MainController',['$scope','campaigns',function ($scope,campaigns) {
    this.awesomeThings = [
      'HTML5 Boilerplate',
      'AngularJS',
      'Karma'
    ];
    var root_uri= '/api/v1/campaigns?limit=15';
    $scope.campaigns = [];
    $scope.page = {};
    $scope.blah = {};

    $scope.$on('filters-updated', function(event, filters){
      $scope.paginate(root_uri+'&'+filters);
    });

    $scope.setData = function(response){
      $scope.campaigns = response.data.objects;
      $scope.page = response.data.meta;
      console.log('yeeeeey!!!' + response.status);
    };

    $scope.handleError = function(error){
      $scope.blah = error;
      console.error('Noooo!!! ' + error);
    };

    $scope.paginate= function(uri){
      campaigns.fetch(uri, $scope.setData, $scope.handleError);
    };

    campaigns.fetch(root_uri, $scope.setData, $scope.handleError);
  }])
  .controller('TabController',function(){
    this.tab = 1;
    this.setTab = function(tab){
        this.tab = tab;
    };

    this.isSet= function(tab){
      return this.tab === tab;
    };
  });
