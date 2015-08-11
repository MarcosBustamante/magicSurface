angular.module('magicSurface', ['msajax', 'msvalidator']);
angular.module('magicSurface').factory('MagicSurface', function(){
    var _token;
    var _username;
    var _host = 'http://magicsurfacebr.appspot.com/';
     //var _host = 'http://localhost:8080/';

    function configApp(token, username){
        _token = token;
        _username = username;
    }

    function getToken(){
        return _token;
    }

    function getUsername(){
        return _username;
    }

    function getHost(){
        return _host
    }

    return {
        getHost: getHost,
        getToken: getToken,
        getUsername: getUsername,
        configApp: configApp
    }
});
