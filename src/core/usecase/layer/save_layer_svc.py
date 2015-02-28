# coding utf-8
__author__ = 'bustamante'
from src.core.layer.model import Layer


def save_layer(name, latitude, longitude, radius):
    layer = Layer()
    layer.name = name
    layer.latitude = latitude
    layer.longitude = longitude
    if radius:
        layer.radius = radius
    layer.put()
