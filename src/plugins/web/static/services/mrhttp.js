angular.module('mrhttp', []);
angular.module('mrhttp').factory('MRHttp', function($http){
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

       post : function(url, params){
           if(!params)
                params = {};
           var req = {
               method: 'POST',
               url: url,
               data: params
           };
           return $http(req);
       },

       post_file: function(url, form){
           var options = {
               withCredentials: true,
               headers: {'Content-Type': undefined },
               transformRequest: angular.identity
           };
           return $http.post(url, form, options);
       }
   }
});