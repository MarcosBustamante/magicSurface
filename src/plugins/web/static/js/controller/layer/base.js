angular.module('MixedRealityApp').controller('BaseCtrl', function($scope, LayerApi, MRHttp){
    var image_layer_get_url = '/image_layer/save/get_url';
    var formData = new FormData();

    $scope.listLayers = function(){
        var options = {'include_layers': LayerApi.options.all}
        LayerApi.list(options)
            .success(function(result){
               $scope.layers = result.layers;
            })
            .error(function(){
                console.log('error');
            });
    };
    $scope.listLayers();

    LayerApi.get_upload_url()
        .success(function(result){
            $scope.upload_url = result.upload_url;
        })
        .error(function(result){

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

    $scope.submitLayer = function(){
        $scope.formLayerAtatus = 'vamos salvar';
        LayerApi.save($scope.form)
            .success(function(result){
                $scope.formLayerAtatus = 'Deu certo';
                $scope.listLayers();
            })
            .error(function(result){
                $scope.formLayerAtatus = 'Deu erro';
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
