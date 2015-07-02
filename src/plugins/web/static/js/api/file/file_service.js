/**
 * Created by bustamante on 6/24/15.
 */
angular.module('magicSurface').factory('FileApi',["MSValidator", "FileRestApi", "$timeout", function(MSValidator, FileRestApi, $timeout){

    function save(file, layer){
        var promise = {
            success: function(_func){promise._success = _func},
            error: function(_func){promise._error = _func},
            finally: function(_func){promise._finally = _func}
        };

        $timeout(function(){
            var _rules = {
                isFile: [file],
                hasLayerId: [layer]
            };

            var status = MSValidator.validate(undefined, _rules);

            if(status.isValid)
            {
                var form = new FormData();
                form.append("layerId", isNaN(layer)? layer.id : layer);
                form.append("file", file);

                FileRestApi.getUrl(file)
                    .success(function(result){
                        FileRestApi.save(result.url, form)
                            .success(promise._success)
                            .error(promise._error)
                            .finally(promise._finally);
                    })
                    .error(promise._error)
                    .finally(promise._finally);
            } else {
                if(promise._error) promise._error(status);
                if(promise._finally) promise._finally('');
            }
        });

        return promise;
    }


    return {
        save: save
    }
}]);