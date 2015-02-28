angular.module('MixedRealityApi', ['ajax']);

angular.module('MixedRealityApi').factory('LayerApi', function(Ajax){
    var url_list_layers = '/layer/list';
    var url_get_layers = '/layer/get';
    var url_save_layers = '/layer/save';

    var options = {
        all: 'ALL'
    };

    var list = function(options){
        return Ajax.get(
            url_list_layers,
            {
                'options': angular.toJson(options)
            }
        )
    };

    var get = function(id, options){
        return Ajax.get(
            url_get_layers,
            {
                'id': id,
                'options': angular.toJson(options)
            }
        )
    };

    var save = function(params){
        return Ajax.post(
            url_save_layers,
            params
        )
    };

    return {
        list: list,
        get: get,
        save: save,
        options: options
    };
});
