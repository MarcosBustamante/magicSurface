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

    function get(form){
        var promise = {
            success: function(_func){promise._success = _func},
            error: function(_func){promise._error = _func},
            finally: function(_func){promise._finally = _func}
        };

        $timeout(function(){
            if (form === undefined) form = {};
            var status = MSValidator.validate(form.layerId, {hasId: [form.layerId]});

            if(status.isValid){
                form.layerId = isNaN(form.layerId)? form.layerId.id : form.layerId;
                form.options = form.options === undefined ? {} : form.options;

                LayerRestApi.get(form)
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
            if (form.options === undefined) form.options = {};
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

    function del(form){
        var promise = {
            success: function(_func){promise._success = _func},
            error: function(_func){promise._error = _func},
            finally: function(_func){promise._finally = _func}
        };

        $timeout(function(){
            if(form === undefined) form = {};
            var is_layer_object = angular.isObject(form.layerId) && angular.isUndefined(form.layerId.id);

            if(is_layer_object || !isNaN(form.layerId)){
                if(form.options === undefined) form.options = {};
                form.layerId = isNaN(form.layerId)? form.layerId.id : form.layerId;

                LayerRestApi.del(form)
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
