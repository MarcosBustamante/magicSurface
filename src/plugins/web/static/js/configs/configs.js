angular.module('MagicSurfaceApp', ['ajax']);

angular.module('MagicSurfaceApp').config(function($interpolateProvider){
    $interpolateProvider.startSymbol('{[{');
    $interpolateProvider.endSymbol('}]}');
});


angular.module('MagicSurfaceApp').directive('ngEnter', function() {
    return function(scope, element, attrs) {
        element.bind("keydown keypress", function(event) {
            if(event.which === 13) {
                    scope.$apply(function(){
                            scope.$eval(attrs.ngEnter);
                    });

                    event.preventDefault();
            }
        });
    };
});