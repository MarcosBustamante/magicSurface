# coding utf-8
import webapp2
from src.plugins.web.api import image_layer, layer
from src.plugins.web.layer.home import BasePage
routes = [
    ('/', BasePage),
    ('/image_layer/save', image_layer.SaveImageLayerHandler),
    ('/layer/save', layer.SaveLayerHandler),
    ('/layer/list', layer.ListLayersHandler),
    ('/layer/get', layer.GetLayersHandler),
    ('/layer/get/url', layer.GetUploadUrlHandler),
]

__author__ = 'bustamante'


app = webapp2.WSGIApplication(routes, debug=True)
