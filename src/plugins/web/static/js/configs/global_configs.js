angular.module('MixedRealityApp', ['mrhttp', 'MixedRealityApi']);

angular.module('MixedRealityApp').config(function($interpolateProvider){
    $interpolateProvider.startSymbol('{[{');
    $interpolateProvider.endSymbol('}]}');
});