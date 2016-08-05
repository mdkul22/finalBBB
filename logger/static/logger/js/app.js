angular.module('mainApp', [
  'ui.router',
  'ngResource',
  'mainApp.controllers',
  'logger.services'
])
  .config(function ($httpProvider, $stateProvider, $urlRouterProvider) {
    // Force angular to use square brackets for template tag
    // The alternative is using {% verbatim %}

    // CSRF Support
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';

    // This only works in angular 3!
    // It makes dealing with Django slashes at the end of everything easier.

    // Django expects jQuery like headers
    // $httpProvider.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded;charset=utf-8';

    // Routing

    $urlRouterProvider.otherwise('/');
    $stateProvider
      .state('home', {
        url: '/',
        templateUrl: 'static/logger/partials/chassis.html',
      })
      .state('sensors', {
        url: '/sensors',
        templateUrl: 'static/logger/partials/hexagons.html',
      })
      .state('graph_bms', {
        url: '/graph_bms',
        templateUrl: 'static/logger/partials/graph.html',
        controller:'bmsCtrl',
      })
      .state('graph_mc', {
        url: '/graph_mc',
        templateUrl: 'static/logger/partials/graph.html',
        controller:'mcCtrl',
      })
      .state('graph_mppt', {
        url: '/graph_mppt',
        templateUrl: 'static/logger/partials/graph.html',
        controller:'mpptCtrl',
      })
      .state('graph_solpan', {
        url: '/graph_solpan',
        templateUrl: 'static/logger/partials/graph.html',
        controller:'solpanCtrl',
      })
      .state('graph_motor', {
        url: '/graph_motor',
        templateUrl: 'static/logger/partials/graph.html',
        controller:'motorCtrl',
      })
  });
