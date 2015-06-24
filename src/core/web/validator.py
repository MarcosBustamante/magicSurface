# coding: utf-8
__author__ = 'bustamante'
from src.core.usecase import MSException

WITH_EXCEPTION = True


def _is_number(form, rules):
    wrong_fields = []
    for rule in rules:
        if form.get(rule) and not str(form[rule]).isdigit():
            wrong_fields.append(rule)

    if len(wrong_fields) > 0 and WITH_EXCEPTION:
        raise MSException('A campos que deveriam ser números!', fields=wrong_fields)


def _not_empty(form, rules):
    wrong_fields = []
    for rule in rules:
        if not form.get(rule):
            wrong_fields.append(rule)
    if len(wrong_fields) > 0 and WITH_EXCEPTION:
        raise MSException('Campos obrigatorios!', fields=wrong_fields)


def validate(form, rules, with_exception=True):
    WITH_EXCEPTION = with_exception

    if 'not_empty' in rules:
        _not_empty(form, rules['not_empty'])

    if 'is_number' in rules:
        _is_number(form, rules['is_number'])
