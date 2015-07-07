# coding: utf-8
from google.appengine.ext import ndb
from src.core.usecase import MSException

__author__ = 'bustamante'


class Config(ndb.Model):
    value = ndb.StringProperty()

    @classmethod
    def get(cls, key):
        config = Config.get_by_id(key)
        if config is None:
            raise MSException(u'A chave %s não foi salva nas configurações' % key)
        return config.value

    @classmethod
    def save(cls, key, value):
        Config(
            id=key,
            value=value
        ).put()