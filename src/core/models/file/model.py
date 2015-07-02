# coding: utf-8
from google.appengine.ext import ndb
from src.core.models.layer.model import Layer

__author__ = 'bustamante'

IMAGE = "image"


class File(ndb.Model):
    name = ndb.StringProperty(required=True)
    link = ndb.StringProperty(required=True)
    layer = ndb.KeyProperty(Layer, required=True)
    deleted = ndb.BooleanProperty(default=False)
    created = ndb.DateTimeProperty(auto_now_add=True)
    last_update = ndb.DateTimeProperty(auto_now=True)

    def to_dict_json(self):
        return {
            'name': self.name,
            'link': self.link,
            'layer': self.layer.id(),
            'deleted': self.deleted,
            'created': str(self.created),
            'last_update': str(self.last_update)
        }

class Image(File):
    blob = ndb.BlobKeyProperty(required=True)
    size = ndb.IntegerProperty(required=True)
    kind = ndb.StringProperty(default=IMAGE)

    def to_dict_json(self):
        _return = super(Image, self).to_dict_json()
        _return.update({
            'size': self.size,
            'kind': self.kind
        })
        return _return

#     images.get_serving_url(blob_key)
# from google.appengine.api import images
