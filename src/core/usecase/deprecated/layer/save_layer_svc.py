# coding utf-8
__author__ = 'bustamante'
from core.models.deprecated.layer.model import Layer


def save_layer(name, latitude, longitude, radius):
    layer = Layer()
    layer.name = name
    layer.latitude = float(latitude)
    layer.longitude = float(longitude)
    if radius:
        layer.radius = float(radius)
    layer.put()
