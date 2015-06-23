# coding: utf-8
import json
import random
import logging
import functools
import traceback
from src.core.models.app.model import App
from src.core.models.user.model import User
from src.core.models.activityLog.model import ActivityLog
from src.core.usecase import MSException
from src.core.web.mshandler import MSHandler

__author__ = 'bustamante'


def callable_from_browser(view_func):
    def _decorated(self):
        self.response.headers['Access-Control-Allow-Origin'] = '*'
        self.response.headers['Access-Control-Allow-Methods'] = 'get,post,options'
        self.response.headers['Access-Control-Allow-Headers'] = 'Origin, X-Requested-With, Content-Type, Accept, X-PINGOTHER, X-CSRFToken'
        view_func(self)

    _decorated.__doc__ = view_func.__doc__
    return _decorated


def ajax_error(method):
    def wrapper(self, *args, **kwargs):
        try:
            method(self, *args, **kwargs)
        except BaseException as e:
            h = MSHandler()
            h.handler = self
            error = {}
            if hasattr(e, 'usr_message'):
                error['msg'] = e.usr_message
                if hasattr(e, 'more_info'):
                    error['more_info'] = e.more_info
                if hasattr(e, 'fields'):
                    error['fields'] = e.fields
            else:
                error['unique_code'] = str(random.getrandbits(18))
                error['msg'] = 'Erro desconhecido [codigo = %s] Erro desconhecido' % error['unique_code']
                logging.error(error['msg'])
                logging.error(traceback.format_exc())

            self.response.set_status(e.http_status_code if hasattr(e, 'http_status_code') else 500)
            self.response.write(json.dumps(error))
    return functools.update_wrapper(wrapper, method)


def no_logged_user(method):
    def wrapper(self, *args, **kwargs):
        user = self.get_logged_user()
        if not user:
            method(self, *args, **kwargs)
        else:
            self.redirect('/myApps')
    return functools.update_wrapper(wrapper, method)


def logged_user(method):
    def wrapper(self, *args, **kwargs):
        user = self.get_logged_user()
        if user:
            method(self, *args, **kwargs)
        else:
            raise MSException(u'O usuário deve estar logado')
    return functools.update_wrapper(wrapper, method)


def app_data_required(activity):
    def decorator(method):
        def wrapper(self, *args, **kwargs):
            body = json.loads(self.request.body) if is_json(self.request.body) else {}
            token = self.request.GET.get('token') or body.get('token')
            user_id = self.request.GET.get('user_id') or body.get('user_id')

            if not token or not user_id:
                raise MSException(u'App token e o user_id devem ser enviados')

            app = App.query(App.token == token).get()
            user = User.get_by_id(user_id)

            if app and user and not app.deleted:
                app_data = {
                    'app': app.to_dict_json(),
                    'user': user.to_dict_json()
                }

                method(self, app_data, *args, **kwargs)

                ActivityLog.save(user_id=user_id, app_name=app.name,token=token, activity=activity)
            else:
                raise MSException(u'App token e o user_id invalido')

        return functools.update_wrapper(wrapper, method)
    return decorator


def is_json(myjson):
    try:
        json.loads(myjson)
        return True
    except ValueError as e:
        return False
