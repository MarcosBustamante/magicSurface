__author__ = 'bustamante'
import os
import json
import webapp2
from src.core.models.user.model import User
from jinja2 import Environment, FileSystemLoader

absolute_path = os.path.abspath(__file__)
template_dir = os.path.sep.join(absolute_path.split(os.path.sep)[:-3] + ['plugins/web/templates'])
environment = Environment(loader=FileSystemLoader(template_dir))


class MSHandler(webapp2.RequestHandler):
    def options(self):
        self.response.headers['Access-Control-Allow-Origin'] = '*'
        self.response.headers['Access-Control-Allow-Methods'] = 'get,post,options'
        self.response.headers['Access-Control-Allow-Headers'] = 'Origin, X-Requested-With, Content-Type, Accept, X-PINGOTHER, X-CSRFToken'
    
    def write_template(self, template, params=None):
        if not params:
            params = {}
        params = self._write_response_params(params)
        my_template = environment.get_template(template)
        self.response.write(my_template.render(params))
    
    def _write_response_params(self, params):
        user = self.get_logged_user()
        if user:
            params['user'] = json.dumps(user.to_dict_json())
        return params
    
    def get_logged_user(self):
        user_id = self.request.cookies.get('user_id')
        if user_id:
            user = User.get_by_id(user_id)
            return user
