'use strict';

angular.module('audetemi_app', [
    'ngRoute',
    'ui.router',
    'ngStorage',
    'ngSanitize',
    'auth',
    'home',
    'ngCookies',
    'ui.bootstrap',
    'ngToast',

]).config(
    ['$stateProvider',
        '$locationProvider',
        '$urlRouterProvider',
        '$httpProvider',
        '$sceDelegateProvider',
        function($stateProvider, $locationProvider, $urlRouterProvider, $httpProvider, $sceDelegateProvider) {

            $sceDelegateProvider.resourceUrlWhitelist(['**']);

            $urlRouterProvider.otherwise('/');
            $stateProvider

                .state('login', {
                url: '/',
                templateUrl: '/static/modules/auth/views/login.html',
                controller: 'authCtrl',
                label: 'Home',
            })

            .state('login-home', {
                url: '/login',
                templateUrl: '/static/modules/auth/views/login.html',
                controller: 'authCtrl',
                label: 'Home',
            })

        }
    ]).run(['$http', '$cookies', '$rootScope', '$sessionStorage', '$state', '$window',
    function($http, $cookies, $rootScope, $sessionStorage, $state, $window) {

        $http.defaults.headers.post['X-CSRFToken'] = $cookies.csrftoken;
        $http.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';

        /* $rootScope.endPoint = "http://tml.snaphelpinc.com"; */
        $rootScope.endPoint = "http://localhost:8000";

        $rootScope.$on('$stateChangeSuccess', function(event) {
            if ($sessionStorage.access_token && $state.current.name != 'login') {
                if (!$http.defaults.headers.common['Authorization']) {
                    $http.defaults.headers.common['Content-Type'] = 'application/json';
                    $http.defaults.headers.common['Authorization'] = 'Bearer ' + $sessionStorage.access_token;
                }
            }
        });
    }
]);
