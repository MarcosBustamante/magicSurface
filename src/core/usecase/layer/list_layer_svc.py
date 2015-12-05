# coding utf-8
from src.core.models.layer.model import Layer
from src.core.usecase.file import list_file_svc

__author__ = 'bustamante'

ALL = 'all'


def _list_all_layers(app_id):
    query = Layer.query(Layer.app_id == app_id)
    layers, cursor, more = [], None, True
    while more:
        values, cursor, more = query.fetch_page(1000, cursor=cursor)
        layers += [value.to_dict_json() for value in values]
    return layers


def listing(app_data, filters, options):
    """
        filter:
            deleted: [True | False]

        options:
            include_files: [image | video | all]
            file_deleted: [true | false]
    """
    filters = {} if not filters else filters
    options = {} if not options else options

    result = {
        'layers': _list_all_layers(app_data['app']['id'])
    }
    
    result['layers'] = _apply_filters(result['layers'], filters)
    result.update(_apply_options(result['layers'], options))
    
    return result


def _apply_filters(layers, filters):
    filter_deleted = filters.get('deleted')
    
    if filter_deleted is not None:
        layers = [l for l in layers if l['deleted'] is filter_deleted]
    
    return layers


def _apply_options(layers, options):
    result = {}
    include_files = options.get('include_files')
    file_deleted = options.get('file_deleted')
    
    if include_files is not None:
        files = result.setdefault('file', [])
        for layer in layers:
            _filter = {
                'files': include_files,
                'deleted': file_deleted
            }
            layer_files = list_file_svc.listing(layer['id'], _filter)
            files.extend(layer_files['files'])
    
    return result


