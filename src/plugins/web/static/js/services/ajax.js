angular.module('msajax', []);
angular.module('msajax').factory('MSAjax', ["$http", "Upload", function($http, Upload){
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

       post_file: function(url, file, data){
           if(!data)
                data = {};
           var req = {
               url: url,
               fields: data,
               file: file
           };

           return Upload.upload(req);
       }
    }
}]);