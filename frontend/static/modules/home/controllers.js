angular.module('home.controller', [])
    .controller('homeCtrl', ['$scope', '$sessionStorage', '$state', '$http',
        function($scope, $sessionStorage, $state, $http) {
//            $scope.personal_info = $sessionStorage.personal_info;
//            $scope.helpers = audetemiHelper.helpers;

//            var agents_my_products = agentHomeService.get_my_products();
//            agents_my_products.then(function(response) {
//                $scope.agents_my_products_tickets = response.data;
//            });

            function range(start, count) {
                return Array.apply(0, Array(count))
                    .map(function(element, index) {
                        return index + start;
                    });
            }

//            var latest_updated_tickets = agentHomeService.getAgentTickets();
//            latest_updated_tickets.then(function(response) {
//                $scope.agents_latest_updated_tickets = response.data;
//                $scope.agents_latest_updated_tickets = $scope.agents_latest_updated_tickets.slice(0, 3);
//            });
        }
    ]);


