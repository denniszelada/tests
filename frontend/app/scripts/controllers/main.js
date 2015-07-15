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
  });
  $scope.campaigns = [];
  $scope.page = {};
  $scope.blah = {};

  campaigns.then(function(response){
    $scope.campaigns = response.data.objects;
    $scope.page = response.data.meta;
    console.log('Ok!!!' + response.status);
  }, function(error){
     $scope.blah = error;
     console.error('Error!!!' + error);
   });
 }]);
