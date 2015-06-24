# coding utf-8
__author__ = 'bustamante'
from google.appengine.ext import ndb
from google.appengine.api import images


class ImageLayer(ndb.Model):
    link = ndb.StringProperty(required=True)
    blob_key = ndb.BlobKeyProperty(required=True)
    layer = ndb.KeyProperty(Layer, required=True)
    creation = ndb.DateTimeProperty(auto_now_add=True)
    last_update = ndb.DateTimeProperty(auto_now=True)

    def to_dict_json(self):
        return {
            'id': self.key.id(),
            'link': self.link,
            'layer_id': self.layer.id(),
            'creation': str(self.creation),
            'last_update': str(self.last_update)
        }

    @staticmethod
    def _get_url(blob_key):
        return images.get_serving_url(blob_key)

    @classmethod
    def get_query(cls, **kwargs):
        q = cls.query()
        if 'layer_key' in kwargs:
            q = q.filter(cls.layer == kwargs['layer_key'])
        return q

