__author__ = 'bustamante'
from google.appengine.ext import blobstore
from google.appengine.api.app_identity import app_identity
from src.core.usecase import UPLOAD_URI
from google.appengine.api import images
from src.core.layer.model import Layer, ImageLayer


def save(blob_info, layer_name):
    link = images.get_serving_url(blob_info.key())
    layer = Layer.find_or_create(layer_name)

    image_layer = ImageLayer()
    image_layer.link = link
    image_layer.layer = layer.key
    image_layer.blob_key = blob_info.key()
    image_layer.put()


def get():
    bucket_name = app_identity.get_default_gcs_bucket_name()
    upload_url = blobstore.create_upload_url(UPLOAD_URI, gs_bucket_name=bucket_name)
    return {'upload_url': upload_url}
