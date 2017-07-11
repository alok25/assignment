'use strict';

angular.module('home', [
    'home.controller'
]).config(
    ['$stateProvider',
     '$urlRouterProvider',
     '$httpProvider',
     function($stateProvider, $urlRouterProvider, $httpProvider) {

        $urlRouterProvider.otherwise('/');
        $stateProvider

        .state('homepage', {
            url: '/homepage',
            cache: false,
            templateUrl: '/static/modules/home/views/home.html',
            controller: 'homeCtrl',
            label: 'Home',
        })
    }]);
