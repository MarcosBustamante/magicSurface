# coding utf-8
from src.core.models.file.model import File
from src.core.models.layer.model import Layer
from src.core.usecase import MSException
from src.core.usecase.file import delete_file_svc

__author__ = 'bustamante'


def delete(app_data, layer_id, options):
    """
        options:
            delete_cascade = [true | false]
    """
    result = {}
    layer = Layer.get_by_id(layer_id)

    if layer is None or layer.app_id != app_data['app']['id']:
        raise MSException('LayerId invalido')

    if layer.deleted:
        raise MSException('Layer ja foi deletado')

    if options.get('delete_cascade', False):
        result['files'] = _delete_files(layer)

    layer.deleted = True
    layer.put()

    result['layer'] = layer.to_dict_json()
    return result


def _delete_files(layer):
    files = File.query(File.layer == layer.key).fetch()
    files_tdj = delete_file_svc.delete(files)
    return files_tdj['files']
