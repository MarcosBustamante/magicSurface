angular.module('MixedRealityApi', ['mrhttp']);

angular.module('MixedRealityApi').factory('LayerApi', function(MRHttp){
    var url_list_layers = '/layer/list';
    var url_get_layers = '/layer/get';
    var url_save_layers = '/layer/save';
    var url_get_upload_url = '/layer/get/url';

    var options = {
        all: 'ALL'
    };

    var list = function(options){
        return MRHttp.get(
            url_list_layers,
            {
                'options': angular.toJson(options)
            }
        )
    };

    var get = function(id, options){
        return MRHttp.get(
            url_get_layers,
            {
                'id': id,
                'options': angular.toJson(options)
            }
        )
    };

    var save = function(params){
        return MRHttp.post(
            url_save_layers,
            params
        )
    };

    var get_upload_url = function(){
        return MRHttp.get(
            url_get_upload_url
        )
    };

    return {
        list: list,
        get: get,
        save: save,
        get_upload_url: get_upload_url,
        options: options
    };
});
