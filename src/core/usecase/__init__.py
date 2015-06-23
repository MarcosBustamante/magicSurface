__author__ = 'bustamante'

class MSException(BaseException):
    def __init__(self, usr_message, fields=None, more_info=None, http_status_code=500):
        BaseException.__init__(self, usr_message)
        self.usr_message = usr_message
        self.more_info = more_info
        self.http_status_code = http_status_code
        self.fields = fields
