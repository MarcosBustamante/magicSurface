angular.module('MixedRealityApp', ['ajax', 'MixedRealityApi']);

angular.module('MixedRealityApp').config(function($interpolateProvider, $httpProvider){
    $interpolateProvider.startSymbol('{[{');
    $interpolateProvider.endSymbol('}]}');
    delete $httpProvider.defaults.headers.common['X-Requested-With'];
});