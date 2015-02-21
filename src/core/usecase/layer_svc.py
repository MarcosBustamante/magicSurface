# coding utf-8
__author__ = 'bustamante'
from src.core.layer.model import Layer, ImageLayer
from src.plugins.web.layer import templates
from google.appengine.ext import ndb
from google.appengine.ext import blobstore
from google.appengine.api.app_identity import app_identity

INCLUDE_ALL = 'ALL'


def save_layer(name, latitude, longitude, radius):
    layer = Layer()
    layer.name = name
    layer.latitude = latitude
    layer.longitude = longitude
    if radius:
        layer.radius = radius
    layer.put()


def _list_all():
    query = Layer.get_query()
    layers, cursor, more = [], None, True
    while more:
        values, cursor, more = query.fetch_page(1000, cursor=cursor)
        layers += [value.to_dict_json() for value in values]
    return layers


def _list_layers(include_layers):
    if include_layers == INCLUDE_ALL:
        return _list_all()


def list_layers(options):
    """
        options:
            include_layers: [ALL]

        Return:
            this method return a to_dict_json layers list
    """

    has_include_layers = 'include_layers' in options
    result = []

    if has_include_layers:
        result.extend(_list_layers(options['include_layers']))

    return result


def _get_images_layers(layer_id, include_images):
    if include_images == INCLUDE_ALL:
        layer_key = ndb.Key(Layer, layer_id)
        query = ImageLayer.get_query(layer_key=layer_key)
        cursor, more, result = None, True, []
        while more:
            values, cursor, more = query.fetch_page(1000, cursor=cursor)
            result.extend([v.to_dict_json() for v in values])
        return result


def get_layers(layer_id, options):
    """
        options:
            include_images: [ALL]

    """
    has_include_images = 'include_images' in options
    result = {}

    if has_include_images:
        result['images'] = _get_images_layers(layer_id, options['include_images'])

    return result


def get_upload_url():
    bucket_name = app_identity.get_default_gcs_bucket_name()
    return blobstore.create_upload_url(templates.UPLOAD_URI, gs_bucket_name=bucket_name)
