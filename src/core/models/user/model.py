# coding utf-8
from webapp2_extras import security
from google.appengine.ext import ndb

__author__ = 'bustamante'


class User(ndb.Model):
    name = ndb.StringProperty(required=True)
    password = ndb.StringProperty(required=True)
    email = ndb.StringProperty(required=True)
    address = ndb.StringProperty(default='')
    number = ndb.IntegerProperty(default=0)
    neighborhood = ndb.StringProperty(default='')
    city = ndb.StringProperty(default='')
    country = ndb.StringProperty(default='')
    birth = ndb.DateProperty()
    created = ndb.DateTimeProperty(auto_now_add=True)
    last_update = ndb.DateTimeProperty(auto_now=True)

    @classmethod
    def save(cls, form):
        user = User(
            id=form['userId'].lower(),
            email=form['email'],
            name=form.get('name', ''),
            address=form.get('address', ''),
            number=form.get('number', 0),
            neighborhood=form.get('neighborhood', ''),
            city=form.get('city', ''),
            country=form.get('country', ''),
            birth=form.get('birth'),
            password=security.generate_password_hash(form['password'])
        ).put()
        return user

    def to_dict_json(self):
        return {
            'id': self.key.id(),
            'email': self.email,
            'name': self.name,
            'address': self.address,
            'number': self.number,
            'neighborhood': self.neighborhood,
            'city': self.city,
            'country': self.country,
            'birth': str(self.birth),
            'created': str(self.created),
            'last_update': str(self.last_update)
        }

    @classmethod
    def authenticate(cls, user_id, password):
        user = User.get_by_id(user_id)
        return user and security.check_password_hash(password, user.password)
