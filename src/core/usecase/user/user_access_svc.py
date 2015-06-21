# coding: utf-8
from src.core.models.activityLog.model import ActivityLog
from src.core.usecase import MSException
from src.core.models.user.model import User
from src.core.web import cookie

__author__ = 'bustamante'


def sign_in(handler, user_id, password):
    is_authenticate = User.authenticate(user_id, password)

    if not is_authenticate:
        raise MSException(u'Username ou senha incorreto!', more_info={'type': 'authentication'})

    cookie.save_user_cookie(handler, user_id)


def sign_out(handler):
    cookie.delete_user_cookie(handler)
