__author__ = 'iury'
import json
import webapp2
from src.core.usecase import layer_svc


class ListLayersHandler(webapp2.RequestHandler):
    def get(self):
        options = self.request.get('options')
        layers = layer_svc.list_layers(options)
        self.response.write(json.dumps({'layers': layers}))
