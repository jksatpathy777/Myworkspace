(function() {
    'use strict';
    angular.module('MyFirstApp', [])
        .controller('MyFirstController', function($scope) {
            $scope.name = "JaiMatadi";
            $scope.sayHello = function() {
                return "Hello Coursera!";
            }
        });

})();