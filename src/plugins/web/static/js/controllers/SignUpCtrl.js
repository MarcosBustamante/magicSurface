/**
 * Created by bustamante on 6/17/15.
 */

angular.module('MagicSurfaceApp').controller('SignUpCtrl', function($scope, MSAjax){
    $scope.errors = {};

    $scope.save = function(){
        _validateForm();

        if (angular.equals($scope.errors, {})){
            MSAjax.post('/signUp', $scope.form).success(function(result){
                alert('Cadastrado com sucesso');
                $scope.form = {}
            }).error(function(error){
                if(error.more_info)
                    $scope.errors = error.more_info;
                else
                    alert(error.msg);
            })
        }
    };

    $scope.removeError = function(field){
        if ($scope.errors[field])
            delete $scope.errors[field]
    };

    function _validateForm() {
        if (!$scope.form) $scope.form = {};
        var _fieldsRequireds = ['userId', 'confirmPassword', 'password', 'email', 'birth', 'name'];

        if ($scope.form.password !== $scope.form.confirmPassword){
            $scope.errors.password = 'As senhas devem ser iguais';
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
