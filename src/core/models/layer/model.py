# coding utf-8
__author__ = 'bustamante'
from google.appengine.ext import ndb
from google.appengine.api import images


class Layer(ndb.Model):
    app_id = ndb.IntegerProperty(required=True)
    name = ndb.StringProperty(required=True)
    latitude = ndb.FloatProperty(required=True)
    longitude = ndb.FloatProperty(required=True)
    radius = ndb.FloatProperty(default=20)
    deleted = ndb.BooleanProperty(default=False)
    created = ndb.DateTimeProperty(auto_now_add=True)
    last_update = ndb.DateTimeProperty(auto_now=True)

    def to_dict_json(self):
        return {
            'id': self.key.id(),
            'name': self.name,
            'created': str(self.created),
            'last_update': str(self.last_update),
            'latitude': self.latitude,
            'longitude': self.longitude,
            'radius': self.radius,
            'deleted': self.deleted
        }

    @classmethod
    def save(cls, app_id, form):
        layer = Layer(
            name=form.get('name'),
            latitude=form.get('latitude'),
            longitude=form.get('longitude'),
            radius=form.get('radius'),
            app_id=app_id
        ).put()
        return layer
