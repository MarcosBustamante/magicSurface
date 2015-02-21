__author__ = 'bustamante'
from google.appengine.api import images
from src.core.layer.model import Layer, ImageLayer

INCLUDE_ALL = 'all'


def save(blob_info, layer_name):
    link = images.get_serving_url(blob_info.key())
    layer = Layer.find_or_create(layer_name)

    image_layer = ImageLayer()
    image_layer.link = link
    image_layer.layer = layer.key
    image_layer.blob_key = blob_info.key()
    image_layer.put()
