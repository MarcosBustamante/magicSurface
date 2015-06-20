/**
 * Created by bustamante on 6/17/15.
 */

angular.module('MagicSurfaceApp').controller('SignUpCtrl', function($scope, Ajax){
    $scope.errors = {};

    $scope.save = function(){
        _validateForm();

        if (angular.equals($scope.errors, {})){
            Ajax.post('/signUp', $scope.form).success(function(result){
                // TODO: Colocar alert de sucesso
                $scope.form = {}
            }).error(function(error){
                // TODO: Colocar alert de error
                if(error.more_info)
                    $scope.errors = error.more_info;
            })
        }
    };

    $scope.removeError = function(field){
        if ($scope.errors[field])
            delete $scope.errors[field]
    };

    function _validateForm() {
        if (!$scope.form) $scope.form = {};
        var _fieldsRequireds = ['userId', 'password', 'email'];

        if ($scope.form.password !== $scope.form.confirmPassword){
            $scope.errors.password = 'As senhas devem ser iguais';
        }

        if($scope.form.number && isNaN($scope.form.number)) {
            $scope.errors.number = 'Insira apenas números';
        }

        if (!_validateEmail($scope.form.email)){
            $scope.errors.email = 'Email inválido';
        }

        for (var index in _fieldsRequireds) {
            if (!$scope.form[_fieldsRequireds[index]]) {
                $scope.errors[_fieldsRequireds[index]] = 'Campo obrigatório';
            }
        }
    }

    function _validateEmail(email) {
        var re = /^([\w-]+(?:\.[\w-]+)*)@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$/i;
        return re.test(email);
    }
});
