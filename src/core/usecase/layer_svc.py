# coding utf-8
__author__ = 'iury'
from src.core.layer.model import Layer


def _list_all():
    query = Layer.get_query()
    layers, cursor, more = [], None, True
    while more:
        values, cursor, more = query.fetch_page(1000, cursor=cursor)
        layers += [value.to_dict_json() for value in values]
    return layers


def list_layers(options):
    """
        Args:
            options.include_all - include all layers

        Return:
            this method return a to_dict_json layers list
    """

    has_include_all = 'include_all' in options
    result = []

    if has_include_all:
        result.extend(_list_all())

    return result
