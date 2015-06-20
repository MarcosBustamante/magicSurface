angular.module('MagicSurfaceApp', ['ajax']);

angular.module('MagicSurfaceApp').config(function($interpolateProvider){
    $interpolateProvider.startSymbol('{[{');
    $interpolateProvider.endSymbol('}]}');
});