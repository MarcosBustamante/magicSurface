# coding: utf-8
import re
from datetime import datetime
from src.core.models.activityLog.model import ActivityLog
from src.core.models.user.model import User
from src.core.usecase import MSException

__author__ = 'bustamante'


def sign_up(form):
    _validate_form(form)
    user_key = User.save(form)
    user = user_key.get()
    ActivityLog.save(user_id=user.key.id(), activity="SignUp")
    return user.to_dict_json()


def _validate_form(form):
    more_info = {}

    _fieldsRequireds = ['userId', 'confirmPassword', 'password', 'email', 'birth', 'name']
    for field in _fieldsRequireds:
        if not form.get(field):
            more_info[field] = u'Campo obrigatório'

    if form.get('password') and form.get('confirmPassword') and form.get('password') != form.get('confirmPassword'):
        more_info['password'] = 'As senhas devem ser iguais'

    if form.get('userId') and User.get_by_id(form.get('userId')):
        more_info['userId'] = u'O id ja existe'

    if form.get('email') and not re.match(r"[^@]+@[^@]+\.[^@]+", form.get('email')):
        more_info['email'] = u'Email inválido'

    if form.get('birth'):
        form['birth'] = form['birth'].split('T')[0]
        form['birth'] = datetime.strptime(form['birth'], "%Y-%m-%d").date()

    if more_info:
        raise MSException(u'Ha campos com informações inválidas', more_info=more_info)
