# coding: utf-8
from src.plugins.web.handlers import HOME
from src.core.web.mshandler import MSHandler

__author__ = 'bustamante'


class HomePageHandler(MSHandler):
    def get(self):
        self.write_template(HOME)
