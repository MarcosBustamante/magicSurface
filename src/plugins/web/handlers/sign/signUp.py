# coding: utf-8
import json
from src.core.web.decorator import ajax_error, no_logged_user
from src.core.usecase.user import user_register_svc
from src.core.web.mshandler import MSHandler
from src.plugins.web.handlers.sign import SIGN_UP
from src.core.web import cookie

__author__ = 'bustamante'


class SignUpHandler(MSHandler):
    @no_logged_user
    def get(self):
        self.write_template(SIGN_UP)

    @no_logged_user
    @ajax_error
    def post(self):
        form = json.loads(self.request.body)
        user_tdj = user_register_svc.sign_up(form)
        cookie.save_user_cookie(self, user_tdj['id'])
        self.response.out.write(json.dumps(user_tdj))
