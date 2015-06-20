# coding: utf-8
from src.plugins.web.handlers.doc import DOC
from src.core.web.mshandler import MSHandler

__author__ = 'bustamante'


class DocHandler(MSHandler):
    def get(self):
        self.write_template(DOC)

    def post(self):
        pass
