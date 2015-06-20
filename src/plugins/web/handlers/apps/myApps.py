# coding: utf-8
import json
from src.core.usecase.app import save_app_svc, list_app_svc, delete_app_svc
from src.core.web.decorator import ajax_error
from src.core.web.mshandler import MSHandler
from src.plugins.web.handlers.apps import MY_APPS

__author__ = 'bustamante'


class MyAppsHandler(MSHandler):
    def get(self):
        user = self.get_logged_user()
        result = []
        if user:
            result = list_app_svc.listing(user.key.id())

        self.write_template(MY_APPS, {'apps': json.dumps(result)})

    @ajax_error
    def post(self):
        user = self.get_logged_user()

        body = json.loads(self.request.body)
        name = body['name']

        result = save_app_svc.save(user, name)
        self.response.out.write(json.dumps(result))

    @ajax_error
    def delete(self):
        app_id = self.request.GET.get('app_id')
        delete_app_svc.delete(app_id)
