angular.module('authenticate.service',[])
       .factory('authService',[
       '$http',
       '$cookies',
       '$rootScope',
       '$sessionStorage',
       function($http, $cookies, $rootScope, $sessionStorage) {

        var service = {};
        service.validate = Validate;
        return service;

        function Validate(username, password) {
            var payload = "email=" + username + "&password=" + password + "&source=" + "AGENT_APP";
            var url =  $http.post($rootScope.endPoint + '/api/user/login/', payload);
            return url;
        };

}]);