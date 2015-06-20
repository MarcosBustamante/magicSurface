# coding: utf-8
import json
import random
import logging
import functools
import traceback
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
