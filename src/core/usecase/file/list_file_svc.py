# coding: utf-8
from google.appengine.ext import ndb
from src.core.models.file.model import File, VIDEO, IMAGE
from src.core.models.layer.model import Layer

__author__ = 'bustamante'

ALL = 'all'


def listing(layer_id, filters):
    """
        filters:
            file: [image | video | all]
            deleted: [true, false]
    """
    result = {'files': _list_files(layer_id)}
    result['files'] = _apply_filters(result['files'], filters)

    return result
    

def _list_files(layer_id):
    files = File.query(File.layer == ndb.Key(Layer, layer_id)).fetch()
    files_tdj = [f.to_dict_json() for f in files]
    return files_tdj


def _apply_filters(files, filters):
    if filters is None:
        filters = {}

    file_filter = filters.get('files', ALL)
    del_filter = filters.get('deleted')

    if file_filter == VIDEO or file_filter == IMAGE:
        files = [f for f in files if f['kind'] == file_filter]

    if del_filter is True:
        files = [f for f in files if f['deleted']]
    elif del_filter is False:
        files = [f for f in files if not f['deleted']]

    return files
