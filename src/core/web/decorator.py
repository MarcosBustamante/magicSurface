__author__ = 'bustamante'


def callable_from_browser(view_func):
    def _decorated(self):
        self.response.headers['Access-Control-Allow-Origin'] = '*'
        self.response.headers['Access-Control-Allow-Methods'] = 'get,post,options'
        self.response.headers['Access-Control-Allow-Headers'] = 'Origin, X-Requested-With, Content-Type, Accept, X-PINGOTHER, X-CSRFToken'
        view_func(self)

    _decorated.__doc__ = view_func.__doc__
    return _decorated
