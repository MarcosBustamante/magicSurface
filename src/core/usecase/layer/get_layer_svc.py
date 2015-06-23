# coding utf-8
from src.core.models.layer.model import Layer
from src.core.usecase import MSException

__author__ = 'bustamante'


def get(app_data, layer_id):
    result = {'layer': _get_layer_to_dict_json(app_data['app']['id'], layer_id)}
    return result


def _get_layer_to_dict_json(app_id, layer_id):
    layer = Layer.get_by_id(int(layer_id))

    if layer is None or layer.app_id != app_id:
        raise MSException('LayerId invalido')

    return layer.to_dict_json()
