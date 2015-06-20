# coding utf-8
import webapp2
from src.plugins.web.handlers.doc import doc
from src.plugins.web.handlers.apps import myApps
from src.plugins.web.handlers.sign import signUp, signIn, signOut
from src.plugins.web.handlers.home import home

site_routes = [
    ('/', home.HomePageHandler),
    ('/signUp', signUp.SignUpHandler),
    ('/signOut', signOut.SignOutHandler),
    ('/signIn', signIn.SignInHandler),
    ('/myApps', myApps.MyAppsHandler),
    ('/documentation', doc.DocHandler),
]

api_routes = [
    # ('/image_layer/save', image_layer.SaveImageLayerHandler),
    # ('/image_layer/get', image_layer.GetImageLayerHandler),
    # ('/layer/save', layer.SaveLayerHandler),
    # ('/layer/list', layer.ListLayersHandler),
    # ('/layer/get', layer.GetLayersHandler),
]


app = webapp2.WSGIApplication(site_routes + api_routes, debug=True)
