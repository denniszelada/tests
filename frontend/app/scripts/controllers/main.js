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
    var  campaign = this;
    this.campaigns = [];
    this.page = {};
    this.blah = {};

    $scope.$on('filters-updated', function(event, filters){
      campaign.paginate(root_uri+'&'+filters);
    });

    this.setData = function(response){
      campaign.campaigns = response.data.objects;
      campaign.page = response.data.meta;
      console.log('yeeeeey!!!' + response.status);
    };

    this.handleError = function(error){
      campaign.blah = error;
      console.error('Noooo!!! ' + error);
    };

    this.paginate= function(uri){
      campaigns.fetch(uri, campaign.setData, campaign.handleError);
    };

    campaigns.fetch(root_uri,campaign.setData,campaign.handleError);
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
