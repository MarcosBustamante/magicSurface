# coding: utf-8
from src.plugins.web.handlers.apps import MY_APPS
from src.core.web.decorator import ajax_error
from src.core.usecase.user import user_access_svc
from src.core.web.mshandler import MSHandler

__author__ = 'bustamante'


class SignOutHandler(MSHandler):
    @ajax_error
    def get(self):
        user_access_svc.sign_out(self)
        self.redirect('/documentation')
