# coding utf-8
from src.core.models.file.model import File
from src.core.usecase import MSException

__author__ = 'bustamante'


def get(file_id):
    result = {'file': _get_file_to_dict_json(file_id)}
    return result


def _get_file_to_dict_json(layer_id):
    file_inst = File.get_by_id(int(layer_id))

    if file_inst is None:
        raise MSException('FileId invalido')

    return file_inst.to_dict_json()
