# coding utf-8
import webapp2
from src.plugins.web.handlers.api.layer import layer
from src.plugins.web.handlers.api.file import file
from src.plugins.web.handlers.doc import doc
from src.plugins.web.handlers.apps import myApps
from src.plugins.web.handlers.sign import signUp, signIn, signOut

__author__ = 'bustamante'


site_routes = [
    ('/', doc.DocHandler),
    ('/signUp', signUp.SignUpHandler),
    ('/signOut', signOut.SignOutHandler),
    ('/signIn', signIn.SignInHandler),
    ('/myApps', myApps.MyAppsHandler),
    ('/documentation', doc.DocHandler)
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
