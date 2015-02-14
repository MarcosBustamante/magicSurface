# coding utf-8
__author__ = 'bustamante'
import webapp2
import json
from google.appengine.ext import blobstore
from src.plugins.web.layer import templates
from src.core.usecase import image_layer_svc
from google.appengine.api.app_identity import app_identity
from google.appengine.ext.webapp import blobstore_handlers


class GetUploadUrlHandler(webapp2.RequestHandler):
    def get(self):
        url = _get_blob_url_upload()
        self.response.write(json.dumps({'url': url}))


class SaveImageLayerHandler(blobstore_handlers.BlobstoreUploadHandler):
    def post(self):
        layer = json.loads(self.request.get('layer'))
        blob_info = self.get_uploads('file')[0]
        image_layer_svc.save(blob_info, layer['name'])

        url = _get_blob_url_upload()
        self.response.write(json.dumps({'new_url': url}))


class ListImagesLayerHandler(webapp2.RequestHandler):
    def get(self):
        layer_name = self.request.get('layer_name') if self.request.get('layer_name') else 'all'
        result = image_layer_svc.list_image_layer(include_images=layer_name)
        self.response.write(json.dumps({'images': result}))


def _get_blob_url_upload():
    bucket_name = app_identity.get_default_gcs_bucket_name()
    return blobstore.create_upload_url(templates.UPLOAD_URI, gs_bucket_name=bucket_name)
