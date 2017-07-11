angular.module('auth.controller', ['auth.services'])
    .controller('authCtrl', ['$scope',
        '$sessionStorage',
        '$state',
        '$http',
        '$location',
        'authService',
        '$timeout',

        function($scope, $sessionStorage, $state, $http, $location, authService, $timeout) {

            // $scope.user_login = function(user_username, user_password, state) {
            //     var response = authService.validate(url_dict.username, url_dict.password);
            //     response.then(function success(response) {
            //         if (response.data) {
            //             var access_token = response.data.access_token;
            //             $sessionStorage.access_token = access_token;
            //             $sessionStorage.personal_info = response.data.personal_info;
            //             $http.defaults.headers.common['Content-Type'] = 'application/json';
            //             $http.defaults.headers.common['Authorization'] = 'Bearer ' + $sessionStorage.access_token;
            //             $state.go('homepage');
            //         } else {
            //             alert("Username and Password do not match !");
            //         }
            //     }, function error(response) {
            //         alert("Username and Password do not match !");
            //     })
            // };

            // if ($location.absUrl().split("?")[1]) {
            //     var sub_url = $location.absUrl().split("?")[1].split("#")[0];
            //     var sub_url = sub_url.split("&");
            //     var url_dict = {};

            //     for (var i = 0; i < sub_url.length; i++) {
            //         if (sub_url[i].split("=")[0] && sub_url[i].split("=")[1]) {
            //             url_dict[sub_url[i].split("=")[0]] = sub_url[i].split("=")[1];
            //         }
            //     }

            //     /*Login through accesstoken */
            //     if (url_dict.username && url_dict.password && url_dict.sr_no) {
            //         $sessionStorage.sr_no = url_dict.sr_no;
            //         $sessionStorage.direct_login = true;
            //         $scope.user_login(url_dict.username, url_dict.password, 'header.leftnav.myincident');
            //     }

            //     /*Login through Username and Password in URL Params*/

            //     if (url_dict.username && url_dict.password && !url_dict.sr_no) {
            //         $sessionStorage.normal_login = true;
            //         $scope.user_login(url_dict.username, url_dict.password, 'header.leftnav.agentHome');
            //     }
            // }

            $scope.submit = function() {

                $scope.isInvalid = false;

                if ($scope.email && $scope.password) {
                    var response = authService.validate($scope.email, $scope.password);
                    response.then(function success(response) {
                        if (response.data && response.data.access_token) {
                            var access_token = response.data.access_token;
                            $sessionStorage.access_token = access_token;
                            $sessionStorage.personal_info = response.data.personal_info;
                            $sessionStorage.normal_login = true;
                            $state.go('homepage');
                        } else {
                            $scope.isInvalid = true;
                            $scope.messsage = "Username and Password do not match !"
                        }
                    }, function error(response) {
                        $state.go('homepage');
                        //$scope.isInvalid = true;
                        //$scope.messsage = "Username and Password do not match !"
                    })
                } else {
                    if (!$scope.email) {
                        $scope.messsage = "Please enter your email"
                    }
                    if (!$scope.password) {
                        $scope.messsage = "Please enter your password"
                    }
                    $scope.isInvalid = true;
                }
                $timeout(function() {
                    $state.go('homepage');
                    //$scope.isInvalid = false;
                }, 3000);
            }
        }
    ])
