# coding utf-8
__author__ = 'bustamante'
import json

import webapp2
from google.appengine.ext.webapp import blobstore_handlers

from core.usecase.deprecated.image_layer import image_layer_svc
from src.core.web.decorator import callable_from_browser


class SaveImageLayerHandler(blobstore_handlers.BlobstoreUploadHandler):
    @callable_from_browser
    def post(self):
        layer_id = self.request.get('layer_id')
        blob_info = self.get_uploads('file')[0]

        image_layer_svc.save(blob_info, layer_id)
        result = image_layer_svc.get()
        self.response.write(json.dumps(result))


class GetImageLayerHandler(webapp2.RequestHandler):
    @callable_from_browser
    def get(self):
        result = image_layer_svc.get()
        self.response.write(json.dumps(result))
