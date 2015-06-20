# coding: utf-8
from src.core.models.app.model import App

__author__ = 'bustamante'


def listing(user_id, filters={}):
    """
        filters

        with_deleted: [True | False]
    """
    with_deleted = filters.get('with_deleted', False)

    query = App.query(App.user_id == user_id)
    apps = query.fetch()
    apps_json = [a.to_dict_json() for a in apps]

    if not with_deleted:
        apps_json = [a for a in apps_json if not a['deleted']]

    return apps_json
