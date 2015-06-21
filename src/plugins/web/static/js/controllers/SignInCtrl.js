/**
 * Created by bustamante on 6/18/15.
 */

angular.module('MagicSurfaceApp').controller('SignInCtrl', function($scope, Ajax){
    $scope.errorMsg = '';

    $scope.signIn = function(){
        _validateForm();

        if ($scope.errorMsg === ''){
            Ajax.post('/signIn', $scope.form).success(function(){
                window.location = '/myApps'
            }).error(function(error){
                if(error.more_info && error.more_info.type === 'authentication')
                    $scope.errorMsg = error.msg;
                else
                    alert(error.msg);
            })
        }
    };

    $scope.removeError = function(){
        $scope.errorMsg = '';
    };

    function _validateForm() {
        if (!$scope.form) $scope.form = {};

        $scope.removeError();
        var _fieldsRequireds = ['userId', 'password'];
        for (var index in _fieldsRequireds) {
            if (!$scope.form[_fieldsRequireds[index]]) {
                $scope.errorMsg = 'Username ou senha incorreto!';
            }
        }
    }

    function _validateEmail(email) {
        var re = /^([\w-]+(?:\.[\w-]+)*)@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$/i;
        return re.test(email);
    }
});
