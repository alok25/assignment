angular.module('landing.service',[])
       .factory('landingService',[
       '$http',
       '$cookies',
       '$rootScope',
       '$sessionStorage',
       function($http, $cookies, $rootScope, $sessionStorage) {

        var service = {};
        service.homepage = Homepage;
        return service;

        function Homepage() {
            var payload = "email=" + username + "&password=" + password + "&source=" + "AGENT_APP";
            var url =  $http.post($rootScope.endPoint + '/api/user/login/', payload);
            return url;
        };

}]);