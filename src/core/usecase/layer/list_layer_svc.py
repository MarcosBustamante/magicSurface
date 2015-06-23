# coding utf-8
from src.core.models.layer.model import Layer

__author__ = 'bustamante'


def _list_all_layers(app_id):
    query = Layer.query(Layer.app_id == app_id)
    layers, cursor, more = [], None, True
    while more:
        values, cursor, more = query.fetch_page(1000, cursor=cursor)
        layers += [value.to_dict_json() for value in values]
    return layers


def listing(app_data, filters):
    """
        filter:
            deleted: [True | False]
    """
    filters = {} if not filters else filters

    has_filter_by_deleted = 'deleted' in filters

    result = {
        'layers': _list_all_layers(app_data['app']['id'])
    }

    if has_filter_by_deleted:
        result['layers'] = [l for l in result['layers'] if l['deleted'] is filters['deleted']]

    return result
