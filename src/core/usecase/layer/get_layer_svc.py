# coding utf-8
from src.core.models.layer.model import Layer
from src.core.usecase import MSException
from src.core.usecase.file import list_file_svc

__author__ = 'bustamante'


def get(app_data, layer_id, options):
    """
        options:
            include_files: [image | video | all]
            file_deleted: [true | false]
    """
    result = {'layer': _get_layer_to_dict_json(app_data['app']['id'], layer_id)}
    result.update(_apply_options(result['layer'], options))
    return result


def _get_layer_to_dict_json(app_id, layer_id):
    layer = Layer.get_by_id(int(layer_id))

    if layer is None or layer.app_id != app_id:
        raise MSException('LayerId invalido')

    return layer.to_dict_json()


def _apply_options(layer, options):
    result = {}
    include_files = options.get('include_files')
    file_deleted = options.get('file_deleted')

    if include_files is not None:
        _filter = {
            'files': include_files,
            'deleted': file_deleted
        }
        result = list_file_svc.listing(layer['id'], _filter)

    return result
