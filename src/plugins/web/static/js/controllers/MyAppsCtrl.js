/**
 * Created by bustamante on 6/18/15.
 */

angular.module('MagicSurfaceApp').controller('MyAppsCtrl', function($scope, MSAjax){
    $scope.MS = MS;

    $scope.delete = function(index){
        var app_id = $scope.MS.apps[index].id;
        MSAjax.delete('/myApps', {app_id: app_id}).success(function(){
            $scope.MS.apps.splice(index, 1);
        }).error(function(error){
            alert(error.msg);
        });
    };

    $scope.save = function(){
        if($scope.appName) {
            MSAjax.post('/myApps', {name: $scope.appName}).success(function (result) {
                $scope.MS.apps.push(result);
            }).error(function (error) {
                alert(error.msg);
            });
        }
    };
});

