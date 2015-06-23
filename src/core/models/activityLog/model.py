# coding utf-8
from webapp2_extras import security
from google.appengine.ext import ndb

__author__ = 'bustamante'


class ActivityLog(ndb.Model):
    user_id = ndb.StringProperty(required=True)
    activity = ndb.StringProperty(required=True)
    app_id = ndb.StringProperty()
    app_name = ndb.StringProperty()
    token = ndb.StringProperty()
    created = ndb.DateTimeProperty(auto_now_add=True)

    @classmethod
    def save(cls, **kwargs):
        ActivityLog(
            user_id=kwargs.get('user_id'),
            activity=kwargs.get('activity'),
            app_id=str(kwargs.get('app_id')),
            app_name=str(kwargs.get('app_name')),
            token=str(kwargs.get('token'))
        ).put()
