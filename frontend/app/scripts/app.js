'use strict';

/**
 * @ngdoc overview
 * @name frontendApp
 * @description
 * # frontendApp
 *
 * Main module of the application.
 */
var app = angular
  .module('frontendApp', [
    'ngAnimate',
    'ngRoute',
    '720kb.datepicker'
  ])
  .config(function ($routeProvider) {
    $routeProvider
      .when('/', {
        templateUrl: 'views/main.html',
        controller: 'MainController',
        controllerAs: 'main'
      })
      .otherwise({
        redirectTo: '/'
      });
  });

  app.service('campaigns',['$http',function($http){
      return {fetch: function(uri, success, error){
        $http.get('http://localhost:8000' + uri, {headers:{'Accept':'application/json'}}).then(
          success, error
        );
      }};
  }]);
