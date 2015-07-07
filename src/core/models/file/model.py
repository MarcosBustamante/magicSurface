# coding: utf-8
from google.appengine.ext import ndb
from src.core.models.layer.model import Layer

__author__ = 'bustamante'

IMAGE = "image"
VIDEO = "video"


class File(ndb.Model):
    name = ndb.StringProperty(required=True)
    link = ndb.StringProperty(required=True)
    layer = ndb.KeyProperty(Layer, required=True)
    app_id = ndb.IntegerProperty(required=True)
    deleted = ndb.BooleanProperty(default=False)
    created = ndb.DateTimeProperty(auto_now_add=True)
    last_update = ndb.DateTimeProperty(auto_now=True)
    size = ndb.IntegerProperty(required=True)
    kind = ndb.StringProperty(choices=(IMAGE, VIDEO))

    def to_dict_json(self):
        return {
            'id': self.key.id(),
            'name': self.name,
            'link': self.link,
            'size': self.size,
            'kind': self.kind,
            'layer_id': self.layer.id(),
            'deleted': self.deleted,
            'created': str(self.created),
            'last_update': str(self.last_update)
        }
