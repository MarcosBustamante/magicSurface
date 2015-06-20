# coding: utf-8
from src.core.usecase.app import list_app_svc
from src.core.usecase import MSException
from src.core.models.app.model import App

__author__ = 'bustamante'


def save(user, name):
    exist_app_name = App.exist_app_name(name)

    if exist_app_name:
        raise MSException('Ja existe uma app com esse nome')

    active_apps = list_app_svc.listing(user.key.id())
    if len(active_apps) == 3:
        raise MSException('Ops voce ja possui 3 apps')

    app_key = App.save(user, name)
    app = app_key.get()
    return app.to_dict_json()

