/**
 * Created by bustamante on 6/24/15.
 */
angular.module('magicSurface').factory('FileRestApi', ["MSAjax", "MagicSurface",function(MSAjax, MagicSurface) {
    var ms = MagicSurface;
    var save_file_url = ms.getHost() + "file/upload";
    var file_list_url = ms.getHost() + "file/list";
    var file_delete_url = ms.getHost() + "file/delete";
    var file_get_url = ms.getHost() + "file/get";

    function getData(){
        return {
            user_id: ms.getUsername(),
            token: ms.getToken()
        }
    }

    function save(form){
        console.log(ms);
        form.append('user_id', ms.getUsername());
        form.append('token', ms.getToken());

        return MSAjax.post_file(save_file_url, form);
    }

    function get(form){
        if(!form)
            form = {};

        angular.extend(form, getData());

        return MSAjax.get(file_get_url, form);
    }

    function list(form){
        if(!form)
            form = {};

        angular.extend(form, getData());

        return MSAjax.get(file_list_url, form);
    }

    function del(form){
        if(!form)
            form = {};

        angular.extend(form, getData());

        return MSAjax.get(file_delete_url, form);
    }

    return {
        save: save,
        get: get,
        list: list,
        del: del
    }
}]);

