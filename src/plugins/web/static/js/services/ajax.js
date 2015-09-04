angular.module('msajax', []);
angular.module('msajax').factory('MSAjax', ["$http", function($http){
    return {
       get : function(url, params){
           if(!params)
                params = {};
           var req = {
               method: 'GET',
               url: url,
               params: params
           };
           return $http(req);
       } ,

       post : function(url, data){
           if(!data)
                data = {};
           var req = {
               method: 'POST',
               url: url,
               data: data
           };
           return $http(req);
       },

       delete : function(url, params){
           if(!params)
                params = {};
           var req = {
               method: "delete",
               url: url,
               params: params
           };
           return $http(req);
       },

       post_file: function(url, data){
           if(!data)
                data = {};
           var req = {
               method: 'POST',
               url: url,
               transformRequest: angular.identity,
               headers: {'Content-Type': undefined},
               data: data
           };
           return $http(req);
       }
    }
}]);