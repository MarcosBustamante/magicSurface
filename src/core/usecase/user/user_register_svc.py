# coding: utf-8
import re
from datetime import datetime
from src.core.models.user.model import User
from src.core.usecase import MSException

__author__ = 'bustamante'


def sign_up(form):
    _validate_form(form)
    user_key = User.save(form)
    user = user_key.get()
    return user.to_dict_json()


def _validate_form(form):
    more_info = {}
    if not form.get('password') or not form.get('confirmPassword'):
        more_info['password'] = u'Campo obrigatório'
    elif form.get('password') != form.get('confirmPassword'):
        more_info['password'] = 'As senhas devem ser iguais'

    if not form.get('userId'):
        more_info['userId'] = u'Campo obrigatório'
    elif User.get_by_id(form.get('userId').lower()):
        more_info['userId'] = u'O id ja existe'

    if not form.get('email'):
        more_info['email'] = u'Campo obrigatório'

    if form.get('number') and not str(form.get('number')).isdigit():
        more_info['number'] = u'Insira apenas números'

    if form.get('email') and not re.match(r"[^@]+@[^@]+\.[^@]+", form.get('email')):
        more_info['email'] = u'Email inválido'

    if form.get('birth'):
        form['birth'] = datetime.strptime(form['birth'], "%Y-%m-%d").date()

    if more_info:
        raise MSException(u'A campos com informações inválidas', more_info=more_info)
