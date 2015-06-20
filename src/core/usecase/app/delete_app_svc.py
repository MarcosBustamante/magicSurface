# coding: utf-8
from src.core.models.app.model import App

__author__ = 'bustamante'


def delete(app_id):
    app = App.get_by_id(int(app_id))
    app.deleted = True
    app.put()
