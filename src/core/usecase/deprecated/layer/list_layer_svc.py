# coding utf-8
__author__ = 'bustamante'
from core.usecase.deprecated.layer import INCLUDE_ALL
from core.models.deprecated.layer.model import Layer


def _list_all():
    query = Layer.get_query()
    layers, cursor, more = [], None, True
    while more:
        values, cursor, more = query.fetch_page(1000, cursor=cursor)
        layers += [value.to_dict_json() for value in values]
    return layers


def _list_layers(include_layers):
    if include_layers == INCLUDE_ALL:
        return _list_all()


def list_layers(options=None):
    """
        options:
            include_layers: [ALL]

        Return:
            this method return a to_dict_json layers list
    """

    has_include_layers = 'include_layers' in options
    result = {}

    if has_include_layers:
        result['layers'] = _list_layers(options['include_layers'])

    return result
