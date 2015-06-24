# coding: utf-8
from src.core.models.activityLog.model import ActivityLog

__author__ = 'bustamante'

MAX_AGE = 86400


def save_user_cookie(handler, user_id):
    handler.response.set_cookie('user_id', user_id, max_age=MAX_AGE)
    ActivityLog.save(user_id=user_id, activity="SignIn")


def delete_user_cookie(handler):
    handler.response.delete_cookie('user_id')
    if handler.request.cookies.get('user_id'):
        ActivityLog.save(user_id=handler.request.cookies.get('user_id'), activity="SignOut")
        del handler.request.cookies['user_id']
