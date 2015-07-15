'use strict';
var app = angular.module('frontendApp');
Chart.defaults.global.responsive= true;
Chart.defaults.global.animationSteps= 7;
Chart.defaults.global.animationEasing= 'easeInOutQuart';
Chart.defaults.global.tooltipFillColor= 'rgba(0, 0, 0, 0.66)';

app.controller('ChartController',['$scope','charts', function($scope, charts){
  var chart = this;
  this.chart= {};
  this.data = {};
  this.page = {};

this.setDatasets = function(response){
  chart.data =response.data.objects;
  chart.page = response.data.meta;
  console.log('yeeeeey!!! ' + response.status);
  var canvas = angular.element.find('#mainChart');
  var context = canvas[0].getContext("2d");
  chart.chart = new Chart(context).Line(chart.data, {
  bezierCurve: false
  });
  console.log('ohh yeah! draw that chart');
};

this.handleError = function(err){
  console.error('Noooo!!! ' + err.data);
};

this.paginate = function(uri){
  charts.fetch(uri, chart.setDatasets, chart.handleError);
}
charts.fetch('/api/v1/chart?limit=7', chart.setDatasets, chart.handleError);
}]);
