# coding: utf-8
__author__ = 'bustamante'

MAX_AGE = 86400


def save_user_cookie(handler, user_id):
    handler.response.set_cookie('user_id', user_id, max_age=MAX_AGE)


def delete_user_cookie(handler):
    handler.response.delete_cookie('user_id')
    if handler.request.cookies.get('user_id'):
        del handler.request.cookies['user_id']
