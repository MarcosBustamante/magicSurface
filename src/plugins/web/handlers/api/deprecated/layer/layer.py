__author__ = 'bustamante'
import json

from src.core.web.mshandler import MSHandler
from src.core.web.decorator import callable_from_browser
from core.usecase.deprecated.layer import list_layer_svc, get_layer_svc, save_layer_svc


class ListLayersHandler(MSHandler):
    @callable_from_browser
    def get(self):
        options = json.loads(self.request.get('options'))

        layers = list_layer_svc.list_layers(options)
        self.response.out.write(json.dumps(layers))


class GetLayersHandler(MSHandler):
    @callable_from_browser
    def get(self):
        options = json.loads(self.request.get('options'))
        layer_id = long(self.request.get('id'))

        layers = get_layer_svc.get_layer(layer_id, options)
        self.response.out.write(json.dumps(layers))


class SaveLayerHandler(MSHandler):
    @callable_from_browser
    def post(self):
        request_dict = json.loads(self.request.body)
        name = request_dict.get('name')
        latitude = request_dict.get('latitude')
        longitude = request_dict.get('longitude')
        radius = request_dict.get('radius', None)

        save_layer_svc.save_layer(name, latitude, longitude, radius)
