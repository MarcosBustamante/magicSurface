# coding utf-8
__author__ = 'bustamante'
import webapp2
from google.appengine.ext.webapp import template
from src.plugins.web.layer import templates


class BasePage(webapp2.RedirectHandler):
    def get(self):
        self.response.out.write(template.render(templates.BASE, {}))
