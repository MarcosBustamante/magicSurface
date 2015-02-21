# coding utf-8
__author__ = 'bustamante'
import json
from src.core.usecase import image_layer_svc, layer_svc
from google.appengine.ext.webapp import blobstore_handlers


class SaveImageLayerHandler(blobstore_handlers.BlobstoreUploadHandler):
    def post(self):
        layer = json.loads(self.request.get('layer'))
        blob_info = self.get_uploads('file')[0]
        image_layer_svc.save(blob_info, layer['name'])
        self.response.write(json.dumps({'upload_url': layer_svc.get_upload_url()}))
