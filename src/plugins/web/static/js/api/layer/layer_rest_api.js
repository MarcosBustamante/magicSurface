/**
 * Created by bustamante on 6/21/15.
 */

angular.module('magicSurface').factory('LayerRestApi', ["MSAjax", "MagicSurface",function(MSAjax, MagicSurface) {
    var ms = MagicSurface;
    var layer_delete_url = ms.getHost() + "layer/delete";
    var layer_save_url = ms.getHost() + "layer/save";
    var layer_list_url = ms.getHost() + "layer/list";
    var layer_get_url = ms.getHost() + "layer/get";

    function getData(){
        return {
            user_id: ms.getUsername(),
            token: ms.getToken()
        }
    }

    function save(form){
        if(!form)
            form = {};

        angular.extend(form, getData());

        return MSAjax.post(layer_save_url, form);
    }

    function get(form){
        if(!form)
            form = {};

        angular.extend(form, getData());

        return MSAjax.get(layer_get_url, form);
    }

    function list(form){
        if(!form)
            form = {};

        angular.extend(form, getData());

        return MSAjax.get(layer_list_url, form);
    }

    function del(form){
        if(!form)
            form = {};

        angular.extend(form, getData());

        return MSAjax.get(layer_delete_url, form);
    }

    return {
        del: del,
        save: save,
        list: list,
        get: get

    }
}]);
