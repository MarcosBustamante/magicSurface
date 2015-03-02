angular.module('MixedRealityApp', ['ajax', 'MixedRealityApi']);

angular.module('MixedRealityApp').config(function($interpolateProvider){
    $interpolateProvider.startSymbol('{[{');
    $interpolateProvider.endSymbol('}]}');
});