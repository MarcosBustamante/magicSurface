angular.module('magicSurface', ['ajax']);
angular.module('magicSurface').factory('MagicSurface', function(){
    var _token;
    var _userId;
    var _host = 'http://magicsurfacebr.appspot.com/';

    function configApp(token, userId){
        _token = token;
        _userId = userId;
    }

    function getToken(){
        return _token;
    }

    function getUserId(){
        return _userId;
    }

    function getHost(){
        return _host
    }

    return {
        getHost: getHost,
        getToken: getToken,
        getUserId: getUserId,
        configApp: configApp
    }
});