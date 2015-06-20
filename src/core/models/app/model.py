# coding utf-8
from webapp2_extras import security
from google.appengine.ext import ndb

__author__ = 'bustamante'


class App(ndb.Model):
    name = ndb.StringProperty(required=True)
    lower = ndb.StringProperty(required=True)
    token = ndb.StringProperty(required=True)
    user_id = ndb.StringProperty(required=True)
    deleted = ndb.BooleanProperty(default=False)
    created = ndb.DateTimeProperty(auto_now_add=True)
    last_update = ndb.DateTimeProperty(auto_now=True)

    @classmethod
    def save(cls, user, name):
        app = App(
            user_id=user.key.id(),
            name=name,
            lower=name.lower(),
            token=security.generate_random_string(length=30)
        ).put()
        return app

    def to_dict_json(self):
        return {
            'id': self.key.id(),
            'user_id': self.user_id,
            'name': self.name,
            'token': self.token,
            'deleted': self.deleted,
            'created': str(self.created),
            'last_update': str(self.last_update)
        }

    @classmethod
    def exist_app_name(cls, name):
        query = App.query(App.lower == name.lower())
        return query.get() is not None
