# coding utf-8
from google.appengine.ext import ndb
from src.core.models.file.model import File

__author__ = 'bustamante'


def delete_by_id(files_id):
    if not isinstance(files_id, list):
        files_id = [files_id]

    files_key = [ndb.Key(File, int(fi)) for fi in files_id]
    files_inst = ndb.get_multi(files_key)

    return delete(files_inst)


def delete(files):
    for file_inst in files:
        file_inst.deleted = True

    ndb.put_multi(files)

    return {'files': [f.to_dict_json() for f in files]}
