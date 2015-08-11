/**
 * Created by bustamante on 6/21/15.
 */
angular.module('msvalidator', []);

angular.module('msvalidator').factory('MSValidator', function(){
    var _form = undefined;
    var _status = undefined;

    var _functionsRoles = {
        'notEmpty': function (fields) {
            var _fieldsWrong = [];
            for(var i = 0; i < fields.length; ++i){
                if(!_form[fields[i]]){
                    _fieldsWrong.push(fields[i]);
                }
            }

            if(!angular.equals(_fieldsWrong, [])){
                return {
                    msg: 'Campos obrigatorios!',
                    fields: _fieldsWrong
                }
            }
        },
        'existOnly': function (fields) {
            var _fieldsWrong = [];
            for(var field in _form){
                if(fields.indexOf(field) === -1){
                    _fieldsWrong.push(field);
                }
            }

            if(!angular.equals(_fieldsWrong, [])){
                return {
                    msg: 'A campos que nao deveriam existir no objeto!',
                    fields: _fieldsWrong
                }
            }
        },
        'isNumber': function (fields) {
            var _fieldsWrong = [];
            for(var i = 0; i < fields.length; ++i){
                if(_form[fields[i]] !== undefined && isNaN(_form[fields[i]])){
                    _fieldsWrong.push(fields[i]);
                }
            }

            if(!angular.equals(_fieldsWrong, [])){
                return {
                    msg: 'A campos que deveriam ser números!',
                    fields: _fieldsWrong
                }
            }
        },
        'hasId': function(layer){
            var isLayerObj = angular.isObject(layer) && angular.isUndefined(layer.id);

            if(!isLayerObj && isNaN(layer)){
                 return {
                     msg: 'Obejot não possui um id!'
                 }
            }
        },
        'isFile': function(file){
            if(angular.isArray(file))
                file = file[0];

            var isFile = angular.isObject(file) && (file instanceof File);

            if(!isFile){
                 return {
                     msg: 'File inválido, verifique se ele é do tipo File'
                 }
            }
        }
    };

    function validate(form, rules){
        _form = form;
        _status = {isValid: true};

        for(var rule in rules){
            var array = rules[rule];
            if(_functionsRoles[rule] !== undefined){
                var error = _functionsRoles[rule](array);
                if ( error !== undefined){
                    _status = error;
                    _status.isValid = false;
                    break;
                }
            } else {
                console.error("Ops a rule " + rule + " não existe!!");
            }
        }

        return _status;
    }

    return {
        validate: validate
    }
});
