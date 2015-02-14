angular.module('mrapp', ['mrhttp']);

angular.module('mrapp').config(function($interpolateProvider){
    $interpolateProvider.startSymbol('{[{');
    $interpolateProvider.endSymbol('}]}');
});