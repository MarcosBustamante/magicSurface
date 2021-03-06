# coding utf-8
from src.core.models.layer.model import Layer
from src.core.usecase import MSException
from src.core.web.validator import validate

__author__ = 'bustamante'

RULES = {
    'not_empty': ['name', 'latitude', 'longitude'],
    'is_number': ['latitude', 'longitude', 'radius']
}


def _fix(form):
    form['latitude'] = float(form['latitude'])
    form['longitude'] = float(form['longitude'])
    form['radius'] = float(form['radius']) if form.get('radius') is not None else 20
    return form


def save(app_data, form):
    validate(form, RULES)
    form = _fix(form)
    if 'id' in form:
        layer = Layer.get_by_id(int(form['id']))
        if layer is None:
            raise MSException('layerId invalido')
        layer.name = form.get('name', layer.name)
        layer.latitude = form.get('latitude', layer.latitude)
        layer.longitude = form.get('longitude', layer.longitude)
        layer.radius = form.get('radius', layer.radius)
        layer.put()
    else:
        layer_key = Layer.save(app_data['app']['id'], form)
        layer = layer_key.get()
    return layer.to_dict_json()
