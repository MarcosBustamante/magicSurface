# coding utf-8
from webapp2_extras import security
from google.appengine.ext import ndb

__author__ = 'bustamante'


class User(ndb.Model):
    name = ndb.StringProperty(required=True)
    password = ndb.StringProperty(required=True)
    email = ndb.StringProperty(required=True)
    birth = ndb.DateProperty(required=True)
    created = ndb.DateTimeProperty(auto_now_add=True)
    last_update = ndb.DateTimeProperty(auto_now=True)

    @classmethod
    def save(cls, form):
        user = User(
            id=form['userId'],
            email=form['email'],
            name=form.get('name', ''),
            birth=form.get('birth'),
            password=security.generate_password_hash(form['password'])
        ).put()
        return user

    def to_dict_json(self):
        return {
            'id': self.key.id(),
            'email': self.email,
            'name': self.name,
            'birth': str(self.birth),
            'created': str(self.created),
            'last_update': str(self.last_update)
        }

    @classmethod
    def authenticate(cls, user_id, password):
        user = User.get_by_id(user_id)
        return user and security.check_password_hash(password, user.password)
