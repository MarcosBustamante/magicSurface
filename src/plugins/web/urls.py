# coding utf-8
import webapp2
from src.plugins.web.layer.home import LayerHandler, DownloadImageLayerHandler, UploadImageLayerHandler

__author__ = 'bustamante'

routes = [
    ('/layer', LayerHandler),
    ('/layer/upload', UploadImageLayerHandler),
    ('/layer/download/([^/]+)?', DownloadImageLayerHandler)
]

app = webapp2.WSGIApplication(routes, debug=True)
