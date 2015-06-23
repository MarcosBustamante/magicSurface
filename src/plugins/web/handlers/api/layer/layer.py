# coding: utf-8
import json
from src.core.usecase.layer import save_layer_svc, get_layer_svc, list_layer_svc, delete_layer_svc
from src.core.web.decorator import app_data_required, ajax_error, callable_from_browser
from src.core.web.mshandler import MSHandler

__author__ = 'bustamante'


class LayerSaveHandler(MSHandler):
    @callable_from_browser
    @ajax_error
    @app_data_required(activity='LayerSave')
    def post(self, app_data):
        form = json.loads(self.request.body)
        result = save_layer_svc.save(app_data, form)
        self.response.out.write(json.dumps(result))


class LayerGetHandler(MSHandler):
    @callable_from_browser
    @ajax_error
    @app_data_required(activity='LayerGet')
    def get(self, app_data):
        layer_id = self.request.GET.get('layerId')
        result = get_layer_svc.get(app_data, layer_id)
        self.response.out.write(json.dumps(result))


class LayerListHandler(MSHandler):
    @callable_from_browser
    @ajax_error
    @app_data_required(activity='LayerList')
    def get(self, app_data):
        filters = json.loads(self.request.GET.get('filters'))
        result = list_layer_svc.listing(app_data, filters)
        self.response.out.write(json.dumps(result))


class LayerDeleteHandler(MSHandler):
    @callable_from_browser
    @ajax_error
    @app_data_required(activity='LayerDelete')
    def get(self, app_data):
        layer_id = self.request.GET.get('layerId')
        result = delete_layer_svc.delete(app_data, layer_id)
        self.response.out.write(json.dumps(result))
