# coding: utf-8
import json
from src.core.web.decorator import ajax_error, no_logged_user
from src.core.usecase.user import user_access_svc
from src.core.web.mshandler import MSHandler
from src.plugins.web.handlers.sign import SIGN_IN

__author__ = 'bustamante'


class SignInHandler(MSHandler):
    @no_logged_user
    def get(self):
        self.write_template(SIGN_IN)

    @no_logged_user
    @ajax_error
    def post(self):
        form = json.loads(self.request.body)
        user_access_svc.sign_in(self, form['userId'], form['password'])
