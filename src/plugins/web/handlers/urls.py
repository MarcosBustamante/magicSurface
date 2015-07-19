# coding utf-8
import webapp2
from src.core.web.mshandler import MSHandler
from src.plugins.web.handlers.api.layer import layer
from src.plugins.web.handlers.api.file import file
from src.plugins.web.handlers.doc import doc
from src.plugins.web.handlers.apps import myApps
from src.plugins.web.handlers.sign import signUp, signIn, signOut
import vimeo
import youtube
from requests.packages import urllib3
urllib3.disable_warnings()
from google.appengine.api import urlfetch
urlfetch.set_default_fetch_deadline(60)
__author__ = 'bustamante'

class Teste(MSHandler):
    def get(self):
        self.write_template('teste.html')

    def post(self):
        file_item = self.request.POST.get('file')
        v = vimeo.VimeoClient(
            token="89c113ec6b8847ba634737d3b8e28071",
            key="f0d0349846dce902a20bde2cef98170e76ea92f6",
            secret="DzmUvtyDRHvh1hfo5lhn9Qm9VNZ8h0+Gw9V3hHKSLZQmrXWu00SqCqfsZQ4dJlcJpWtRjE2N+1wPhxa8dP6dI3b0qX/1JqJJIt0i0NRIsqVi+Ivr2+ReGmQlshASrUud")

        v.upload(file_item)

site_routes = [
    ('/', doc.DocHandler),
    ('/signUp', signUp.SignUpHandler),
    ('/signOut', signOut.SignOutHandler),
    ('/signIn', signIn.SignInHandler),
    ('/myApps', myApps.MyAppsHandler),
    ('/documentation', doc.DocHandler),
    ('/teste', Teste)
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
