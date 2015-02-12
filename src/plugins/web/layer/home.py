# coding utf-8
__author__ = 'bustamante'
import urllib
import webapp2
from google.appengine.ext import blobstore
from google.appengine.ext.webapp import template, blobstore_handlers
from google.appengine.api.app_identity import app_identity
from src.plugins.web.layer import templates


class LayerHandler(webapp2.RequestHandler):
    def get(self):
        bucket_name = app_identity.get_default_gcs_bucket_name()
        upload_url = blobstore.create_upload_url(templates.UPLOAD_URI, gs_bucket_name=bucket_name)
        self.response.out.write(template.render(templates.BASE, {'upload_url': upload_url}))


class UploadImageLayerHandler(blobstore_handlers.BlobstoreUploadHandler):
    def post(self):
        upload_file = self.get_uploads('file')
        blob_info = upload_file[0]
        download_url = '%s/%s' % (templates.DOWNLOAD_URI, blob_info.key())
        self.response.out.write(template.render(templates.BASE, {'download_url': download_url}))


class DownloadImageLayerHandler(blobstore_handlers.BlobstoreDownloadHandler):
    def get(self, resource):
        resource = str(urllib.unquote(resource))
        blob_info = blobstore.BlobInfo.get(resource)
        self.send_blob(blob_info)
