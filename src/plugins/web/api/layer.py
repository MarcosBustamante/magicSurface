__author__ = 'bustamante'
import json
from src.core.web.mrhandler import MRHandler
from src.core.web.decorator import callable_from_browser
from src.core.usecase.layer import list_layer_svc, get_layer_svc, save_layer_svc


class ListLayersHandler(MRHandler):
    @callable_from_browser
    def get(self):
        options = json.loads(self.request.get('options'))

        layers = list_layer_svc.list_layers(options)
        self.response.out.write(json.dumps(layers))


class GetLayersHandler(MRHandler):
    @callable_from_browser
    def get(self):
        options = json.loads(self.request.get('options'))
        layer_id = long(self.request.get('id'))

        layers = get_layer_svc.get_layers(layer_id, options)
        self.response.out.write(json.dumps(layers))


class SaveLayerHandler(MRHandler):
    @callable_from_browser
    def post(self):
        form = json.loads(self.request.body)
        name = form.get('name')
        latitude = float(form.get('latitude'))
        longitude = float(form.get('longitude'))
        radius = float(form.get('radius')) if 'radius' in form else None

        save_layer_svc.save_layer(name, latitude, longitude, radius)
