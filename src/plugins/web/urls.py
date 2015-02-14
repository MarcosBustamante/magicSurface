# coding utf-8
import webapp2
from src.plugins.web.api.layer import image_layer_rest_api
from src.plugins.web.api.layer import layer_rest_api
from src.plugins.web.layer.home import BasePage
routes = [
    ('/', BasePage),
    ('/image_layer/save', image_layer_rest_api.SaveImageLayerHandler),
    ('/image_layer/save/get_url', image_layer_rest_api.GetUploadUrlHandler),
    ('/image_layer/list', image_layer_rest_api.ListImagesLayerHandler),
    ('/layer/list', layer_rest_api.ListLayersHandler)
]

__author__ = 'bustamante'


app = webapp2.WSGIApplication(routes, debug=True)
