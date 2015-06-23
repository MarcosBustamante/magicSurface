# coding utf-8
from src.core.models.layer.model import Layer
from src.core.usecase import MSException
from src.core.usecase.layer import get_layer_svc

__author__ = 'bustamante'


def delete(app_data, layer_id):
    layer = Layer.get_by_id(int(layer_id))

    if layer is None or layer.app_id != app_data['app']['id']:
        raise MSException('LayerId invalido')

    if layer.deleted:
        raise MSException('Layer ja foi deletado')

    layer.deleted = True
    layer.put()

    return layer.to_dict_json()
