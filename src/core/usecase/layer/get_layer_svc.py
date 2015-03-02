# coding utf-8
__author__ = 'bustamante'
from src.core.usecase.layer import INCLUDE_ALL
from src.core.layer.model import Layer, ImageLayer
from google.appengine.ext import ndb


def get_layer(layer_id, options):
    """
        filters:
            include_images: [ALL]
    """
    if not options:
        options = {}

    has_include_images = 'include_images' in options
    result = {}

    if has_include_images:
        result['images'] = _get_images_layers(layer_id, options['include_images'])
    result['layer'] = _get_by_id(layer_id)

    return result


def _get_by_id(layer_id):
    layer = Layer.get_by_id(layer_id)
    return layer.to_dict_json()


def _get_images_layers(layer_id, include_images):
    if include_images == INCLUDE_ALL:
        layer_key = ndb.Key(Layer, layer_id)
        query = ImageLayer.get_query(layer_key=layer_key)
        cursor, more, result = None, True, []
        while more:
            values, cursor, more = query.fetch_page(1000, cursor=cursor)
            result.extend([v.to_dict_json() for v in values])
        return result
