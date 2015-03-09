# coding utf-8
import webapp2
from src.plugins.web.api import image_layer, layer
from src.plugins.web.layer.home import BasePage

routes = [
    ('/', BasePage),
    ('/image_layer/save', image_layer.SaveImageLayerHandler),
    ('/image_layer/get', image_layer.GetImageLayerHandler),
    ('/layer/save', layer.SaveLayerHandler),
    ('/layer/list', layer.ListLayersHandler),
    ('/layer/get', layer.GetLayersHandler),
]

__author__ = 'bustamante'


app = webapp2.WSGIApplication(routes, debug=True)
