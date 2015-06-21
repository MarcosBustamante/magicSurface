# coding utf-8
from webapp2_extras import security
from google.appengine.ext import ndb

__author__ = 'bustamante'


class ActivityLog(ndb.Model):
    user_id = ndb.StringProperty(required=True)
    activity = ndb.StringProperty(required=True)
    app_id = ndb.StringProperty()
    created = ndb.DateTimeProperty(auto_now_add=True)

    @classmethod
    def save(cls, **kwargs):
        ActivityLog(
            user_id=kwargs.get('user_id'),
            activity=kwargs.get('activity'),
            app_id=str(kwargs.get('app_id'))
        ).put()
