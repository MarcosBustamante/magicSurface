# coding utf-8
__author__ = 'iury'
from google.appengine.ext import ndb
from google.appengine.api import images


class Layer(ndb.Model):
    name = ndb.StringProperty(required=True)
    creation = ndb.DateTimeProperty(auto_now_add=True)
    last_update = ndb.DateTimeProperty(auto_now=True)

    def to_dict_json(self):
        return {
            'id': self.key.id(),
            'name': self.name,
            'creation': str(self.creation),
            'last_update': str(self.last_update)
        }

    @classmethod
    def find_or_create(cls, layer_name):
        layer = cls.query(cls.name == layer_name).get()
        if layer:
            return layer
        layer = Layer()
        layer.name = layer_name
        layer.put()
        return layer

    @classmethod
    def get_query(cls, **kwargs):
        q = cls.query()
        if 'name' in kwargs:
            q.filter(cls.name == kwargs['name'])
        return q


class ImageLayer(ndb.Model):
    link = ndb.StringProperty(required=True)
    blob_key = ndb.BlobKeyProperty(required=True)
    layer = ndb.KeyProperty(Layer, required=True)
    creation = ndb.DateTimeProperty(auto_now_add=True)
    last_update = ndb.DateTimeProperty(auto_now=True)

    def to_dict_json(self):
        return {
            'image_layer_id': self.key.id(),
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
        if 'layer' in kwargs:
            q.filter(cls.layer == kwargs['layer'])
        return q

