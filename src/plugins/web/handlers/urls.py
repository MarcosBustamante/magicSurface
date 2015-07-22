# coding utf-8

import webapp2
import urllib
from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers
from src.core.web.mshandler import MSHandler
from src.plugins.web.handlers.api.layer import layer
from src.plugins.web.handlers.api.file import file
from src.plugins.web.handlers.doc import doc
from src.plugins.web.handlers.apps import myApps
from src.plugins.web.handlers.sign import signUp, signIn, signOut
from requests.packages import urllib3
urllib3.disable_warnings()


__author__ = 'bustamante'

class Teste(MSHandler):
    def get(self):
        upload_url = blobstore.create_upload_url('/upload')
        self.write_template('teste.html', {'upload_url': upload_url})

class UploadVideo(blobstore_handlers.BlobstoreUploadHandler):
    def post(self):
        upload = self.get_uploads()[0]
        self.redirect('/view_video/%s' % upload.key())

class ViewVideo(blobstore_handlers.BlobstoreDownloadHandler):
    def get(self, video_key):
        self.send_blob(video_key)

site_routes = [
    ('/', doc.DocHandler),
    ('/signUp', signUp.SignUpHandler),
    ('/signOut', signOut.SignOutHandler),
    ('/signIn', signIn.SignInHandler),
    ('/myApps', myApps.MyAppsHandler),
    ('/documentation', doc.DocHandler),
    ('/teste', Teste),
    ('/upload', UploadVideo),
    ('/view_video/([^/]+)?', ViewVideo),
]
api_routes = [
    ('/layer/get', layer.LayerGetHandler),
    ('/layer/list', layer.LayerListHandler),
    ('/layer/save', layer.LayerSaveHandler),
    ('/layer/delete', layer.LayerDeleteHandler),
    ('/file/get', file.FileGetHandler),
    ('/file/list', file.FileListHandler),
    ('/file/upload', file.FileSaveHandler),
    ('/file/delete', file.FileDeleteHandler),
]



app = webapp2.WSGIApplication(site_routes + api_routes, debug=True)
