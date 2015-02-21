__author__ = 'bustamante'
import json
import webapp2
from src.core.usecase import layer_svc


class ListLayersHandler(webapp2.RequestHandler):
    def get(self):
        options = self.request.get('options')
        layers = layer_svc.list_layers(json.loads(options))
        self.response.write(json.dumps({'layers': layers}))


class GetLayersHandler(webapp2.RequestHandler):
    def get(self):
        options = self.request.get('options')
        layer_id = long(self.request.get('id'))
        layers = layer_svc.get_layers(layer_id, json.loads(options))
        self.response.write(json.dumps(layers))


class GetUploadUrlHandler(webapp2.RequestHandler):
    def get(self):
        upload_url = layer_svc.get_upload_url()
        self.response.write(json.dumps({'upload_url': upload_url}))


class SaveLayerHandler(webapp2.RedirectHandler):
    def post(self):
        form = json.loads(self.request.body)
        name = form.get('name')
        latitude = float(form.get('latitude'))
        longitude = float(form.get('longitude'))
        radius = float(form.get('radius')) if 'radius' in form else None

        layer_svc.save_layer(name, latitude, longitude, radius)
