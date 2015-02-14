__author__ = 'iury'
from google.appengine.api import images
from src.core.layer.model import Layer, ImageLayer
INCLUDE_ALL = 'all'


def save(blob_info, layer_name):
    # content_type = blob_info.
    link = images.get_serving_url(blob_info.key())
    layer = Layer.find_or_create(layer_name)

    image_layer = ImageLayer()
    image_layer.link = link
    image_layer.layer = layer.key
    image_layer.blob_key = blob_info.key()
    image_layer.put()


def _list_all():
    query = ImageLayer.get_query()
    cursor, more, result = None, True, []
    while more:
        values, cursor, more = query.fetch_page(1000, cursor=cursor)
        result.extend([v.to_dict_json() for v in values])
    return result


def _list_layer_images(layer_name):
    query = Layer.get_query(name=layer_name)
    layer = query.get()
    query = ImageLayer.get_query(layer=layer.key)
    cursor, more, result = None, True, []
    while more:
        values, cursor, more = query.fetch_page(1000, cursor=cursor)
        result.extend([v.to_dict_json() for v in values])
    return result


def _list_images(layer_name):
    if layer_name == INCLUDE_ALL:
        return _list_all()
    return _list_layer_images(layer_name)


def list_image_layer(**options):
    """
        Args:
            options.include_images: <layer_name | 'all'> - include all layer images or all images

        Return:
            this method return a to_dict_json layers list
    """
    has_layer_name = 'include_images' in options
    result = []

    if has_layer_name:
        result.extend(_list_images(options['include_images']))

    return result
