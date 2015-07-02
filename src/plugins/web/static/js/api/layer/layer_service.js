/**
 * Created by bustamante on 6/21/15.
 */
angular.module('magicSurface').factory('LayerApi', ["LayerRestApi", "MSValidator", "$timeout", function(LayerRestApi, MSValidator, $timeout){
    var _rules = {
        notEmpty: ['name', 'latitude', 'longitude'],
        existOnly: ['name', 'latitude', 'longitude', 'radius', 'id'],
        isNumber: ['latitude', 'longitude', 'radius']
    };

    var _filters = {
        existOnly: ['deleted']
    };

    function save(form){
        var promise = {
            success: function(_func){promise._success = _func},
            error: function(_func){promise._error = _func},
            finally: function(_func){promise._finally = _func}
        };

        $timeout(function(){
            var status = MSValidator.validate(form, _rules);

            if(status.isValid) {
                LayerRestApi.save(form)
                    .success(promise._success)
                    .error(promise._error)
                    .finally(promise._finally);
            } else {
                if(promise._error) promise._error(status);
                if(promise._finally) promise._finally('');
            }
        });

        return promise;
    }

    function get(layer){
        var promise = {
            success: function(_func){promise._success = _func},
            error: function(_func){promise._error = _func},
            finally: function(_func){promise._finally = _func}
        };

        $timeout(function(){
            var status = MSValidator.validate(layer, {hasLayerId: [layer]});
            if(status.isValid){
                var params = {layerId: isNaN(layer)? layer.id : layer};
                LayerRestApi.get(params)
                    .success(promise._success)
                    .error(promise._error)
                    .finally(promise._finally);
            } else {
                if(promise._error) promise._error(status);
                if(promise._finally) promise._finally('');
            }
        });

        return promise
    }

    function list(form){
        var promise = {
            success: function(_func){promise._success = _func},
            error: function(_func){promise._error = _func},
            finally: function(_func){promise._finally = _func}
        };

        $timeout(function(){
            if (form === undefined) form = {};
            if (form.filters === undefined) form.filters = {};
            var status = MSValidator.validate(form.filters, _filters);

            if(status.isValid) {
                LayerRestApi.list(form)
                    .success(promise._success)
                    .error(promise._error)
                    .finally(promise._finally);
            } else {
                if(promise._error) promise._error(status);
                if(promise._finally) promise._finally('');
            }
        });

        return promise;
    }

    function del(layer){
        var promise = {
            success: function(_func){promise._success = _func},
            error: function(_func){promise._error = _func},
            finally: function(_func){promise._finally = _func}
        };

        $timeout(function(){
            var is_layer_object = angular.isObject(layer) && angular.isUndefined(layer.id);
            if(is_layer_object || !isNaN(layer)){
                var params = {layerId: isNaN(layer)? layer.id : layer};
                LayerRestApi.del(params)
                    .success(promise._success)
                    .error(promise._error)
                    .finally(promise._finally);
            } else {
                if(promise._error) promise._error({msg: 'LayerId inválido'});
                if(promise._finally) promise._finally('');
            }
        });

        return promise
    }

    return {
        save: save,
        list: list,
        get: get,
        del: del
    }
}]);
