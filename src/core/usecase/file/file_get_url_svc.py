# coding: utf-8
from google.appengine.api import app_identity, blobstore
from src.core.usecase import MSException
from src.core.models.file.model import IMAGE

# HOST = http://magicsurfacebr.appspot.com/
HOST = 'http://localhost:8080/'

__author__ = 'bustamante'

def get(arq):
    kind = _get_file_kind(arq)

    if kind == IMAGE:
        return _get_image_upload_url()


def _get_file_kind(file):
    name_extencion = file['name'].split('.')[-1]
    file_type = file['type'].split('/')[-1]

    if _is_image(name_extencion) and _is_image(file_type):
        return IMAGE
    else:
        raise MSException('Arquivo inválido! verifique se ele eh do tipo: jpg ou png')


def _is_image(extencion):
    return extencion.lower() in ['jpeg', 'jpg', 'png']


def _get_image_upload_url():
    bucket_name = app_identity.get_default_gcs_bucket_name()
    return blobstore.create_upload_url('%sfile/upload/image' % HOST, gs_bucket_name=bucket_name)
