__author__ = 'bustamante'
import webapp2


class MRHandler(webapp2.RequestHandler):
    def options(self):
        self.response.headers['Access-Control-Allow-Origin'] = '*'
        self.response.headers['Access-Control-Allow-Methods'] = 'get,post,options'
        self.response.headers['Access-Control-Allow-Headers'] = 'Origin, X-Requested-With, Content-Type, Accept, X-PINGOTHER, X-CSRFToken'
