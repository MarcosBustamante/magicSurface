# coding utf-8
import json
from src.core.usecase.file import save_file_svc, list_file_svc, delete_file_svc, get_file_svc
from src.core.web.decorator import ajax_error, callable_from_browser, app_data_required
from src.core.web.mshandler import MSHandler

__author__ = 'bustamante'


class FileSaveHandler(MSHandler):
    @callable_from_browser
    @ajax_error
    @app_data_required(activity='FileSave')
    def post(self):
        data = self.get_app_data()
        data.update({
            'angle_x': self.request.POST.get('angle_x'),
            'angle_y': self.request.POST.get('angle_y'),
            'angle_z': self.request.POST.get('angle_z'),
            'layerId': self.request.POST.get('layerId'),
        })

        file_item = self.request.POST.get('file')

        result = save_file_svc.save(data, file_item)
        self.response.out.write(json.dumps(result))


class FileGetHandler(MSHandler):
    @callable_from_browser
    @ajax_error
    @app_data_required(activity='FileGet')
    def get(self):
        file_id = self.request.GET.get('fileId')

        result = get_file_svc.get(file_id)
        self.response.out.write(json.dumps(result))


class FileListHandler(MSHandler):
    @callable_from_browser
    @ajax_error
    @app_data_required(activity='FileList')
    def get(self):
        layer_id = int(self.request.GET.get('layerId'))
        filters = json.loads(self.request.GET.get('filters'))
        result = list_file_svc.listing(layer_id, filters)
        self.response.out.write(json.dumps(result))


class FileDeleteHandler(MSHandler):
    @callable_from_browser
    @ajax_error
    @app_data_required(activity='FileDelete')
    def get(self):
        file_id = self.request.GET.get('FileId') or self.request.GET.get('FilesId')
        result = delete_file_svc.delete_by_id(file_id)
        self.response.out.write(json.dumps(result))
