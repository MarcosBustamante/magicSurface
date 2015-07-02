/**
 * Created by bustamante on 6/24/15.
 */
angular.module('magicSurface').factory('FileRestApi', ["MSAjax", "MagicSurface",function(MSAjax, MagicSurface) {
    var ms = MagicSurface;
    var file_geUrl_url = ms.getHost() + "file/upload/url";

    function getData(){
        return {
            user_id: ms.getUsername(),
            token: ms.getToken()
        }
    }

    function getUrl(file){
        var form = {file: file};

        angular.extend(form, getData());

        return MSAjax.get(file_geUrl_url, form);
    }

    function save(url, form){
        form.append('user_id', ms.getUsername());
        form.append('token', ms.getToken());

        return MSAjax.post_file(url, form)
    }

    return {
        getUrl: getUrl,
        save: save

    }
}]);

