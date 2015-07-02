# coding utf-8
import json
from google.appengine.ext.webapp import blobstore_handlers
import webapp2
from src.core.usecase.file import file_get_url_svc
from src.core.web.decorator import ajax_error, callable_from_browser, app_data_required
from src.core.web.mshandler import MSHandler

__author__ = 'bustamante'


class FileGetUrlHandler(MSHandler):
    @callable_from_browser
    @ajax_error
    @app_data_required(activity='FileGetUrl')
    def get(self, app_data):
        arq = json.loads(self.request.GET.get('file'))
        url = file_get_url_svc.get(arq)
        self.response.out.write(json.dumps({'url': url}))


class FileSaveImagelHandler(blobstore_handlers.BlobstoreUploadHandler):
    @callable_from_browser
    @ajax_error
    @app_data_required(activity='FileSaveImage')
    def post(self):
        layer_id = self.request.get('layerId')
        blob_info = self.get_uploads('file')[0]
        #
        # image_layer_svc.save(blob_info, layer_id)
        # result = image_layer_svc.get()
        # self.response.write(json.dumps(result))





# import json
#
# import webapp2
# from google.appengine.ext.webapp import blobstore_handlers
#
# from src.core.web.decorator import callable_from_browser
#
#
# class SaveImageLayerHandler(blobstore_handlers.BlobstoreUploadHandler):
#     @callable_from_browser
#     def post(self):
#         layer_id = self.request.get('layer_id')
#         blob_info = self.get_uploads('file')[0]
#
#         image_layer_svc.save(blob_info, layer_id)
#         result = image_layer_svc.get()
#         self.response.write(json.dumps(result))
#
#
# class GetImageLayerHandler(webapp2.RequestHandler):
#     @callable_from_browser
#     def get(self):
#         result = image_layer_svc.get()
#         self.response.write(json.dumps(result))
# from google.appengine.ext import blobstore
# from google.appengine.api.app_identity import app_identity
# from google.appengine.api import images
#
# from src.core.usecase import UPLOAD_URI
# from core.models.deprecated.layer.model import Layer, ImageLayer
#
#
# def save(blob_info, layer_id):
#     link = images.get_serving_url(blob_info.key())
#     layer = Layer.get_by_id(int(layer_id))
#
#     image_layer = ImageLayer()
#     image_layer.link = link
#     image_layer.layer = layer.key
#     image_layer.blob_key = blob_info.key()
#     image_layer.put()
#
#
# def get():
#     bucket_name = app_identity.get_default_gcs_bucket_name()
#     upload_url = blobstore.create_upload_url(UPLOAD_URI, gs_bucket_name=bucket_name)
#     return {'upload_url': upload_url}