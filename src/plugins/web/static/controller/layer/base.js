angular.module('mrapp').controller('BaseCtrl', function($scope, MRHttp, $http){
    var list_layers = '/layer/list';
    var image_layer_get_url = '/image_layer/save/get_url';
    var image_layer_list = '/image_layer/list';
    var formData = new FormData();

    var params = {'options': ['include_all']};
    MRHttp.get(list_layers, params)
        .success(function(result){
           $scope.layers = result.layers;
        })
        .error(function(){
            console.log('error');
        });

    MRHttp.get(image_layer_get_url)
        .success(function(result){
            $scope.upload_url = result['url'];
        });

    $scope.uploadFile = function(files) {
        formData.append("file", files[0]);
    };

    $scope.submitForm = function(){
        $scope.status = 'Mandando para o servidor';
        formData.append("layer", angular.toJson($scope.my_layer));
        MRHttp.post_file($scope.upload_url, formData).success(function(result){
            $scope.upload_url = result.new_url;
            $scope.status = 'Salvo com sucesso';
        }).error(function(){
                $scope.status = 'Ocorreu um erro';
            });
    };

    $scope.getImages = function(layer){
        MRHttp.get(image_layer_list, {'layer_name': layer.name})
            .success(function(result){
            $scope.images = result.images;
        });
    };
});
