angular.module('MixedRealityApp').controller('BaseCtrl', function($scope, ImageLayerApi, LayerApi, Ajax){
    var formData = new FormData();

//    Pegando todos os layers
    $scope.listLayers = function(){
        var options = {'include_layers': LayerApi.options.all}
        LayerApi.list(options)
            .success(function(result){
               $scope.layers = result.layers;
            });
    }();

//  Pegando a url para efetuar o upload
    $scope.get_upload_url = function(){
        ImageLayerApi.get()
            .success(function(result){
                $scope.upload_url = result.upload_url;
            });
    }();

    $scope.uploadFile = function(files) {
        formData.append("file", files[0]);
    };

    $scope.submitForm = function(){
        $scope.status = 'Mandando para o servidor';
        formData.append("layer_id", angular.toJson($scope.my_layer.id));
        Ajax.post_file($scope.upload_url, formData)
            .success(function(result){
                $scope.upload_url = result.upload_url;
                $scope.status = 'Salvo com sucesso';
            }).error(function(){
                $scope.status = 'Ocorreu um erro';
            });
    };

    $scope.submitLayer = function(){
        $scope.formLayerStatus = 'vamos salvar';
        LayerApi.save($scope.form)
            .success(function(result){
                $scope.formLayerStatus = 'Deu certo';
                $scope.listLayers();
            })
            .error(function(result){
                $scope.formLayerStatus = 'Deu erro';
            });
    };

    $scope.getImages = function(layer){
        var options = {'include_images': LayerApi.options.all};
        LayerApi.get(layer.id, options)
            .success(function(result){
                $scope.images = result.images;
            });
    };
});
