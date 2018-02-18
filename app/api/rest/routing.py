"""
REST API Resource Routing

http://flask-restful.readthedocs.io/en/latest/
"""

import time
from flask import request
from app.api.rest.base import BaseResource, SecureResource, rest_resource
from app.components.aliyun_ots import OTSTools
from app.components.aliyun_iot import IotServer
from config.path import APP_PATH
import json


@rest_resource
class DeviceLog(BaseResource):
    """ /api/resource/one """
    endpoints = ['/device/log']

    def __init__(self):
        self.ots_client = OTSTools.get_instance()

    def get(self):
        return self.ots_client.get_last_limit_row()


@rest_resource
class DeviceStat(BaseResource):
    """ /api/resource/one """
    endpoints = ['/device/stat']

    def __init__(self):
        self.iot_server = IotServer.get_instance()

    def get(self):
        data = self.iot_server.get_device_stat()
        return {'errcode': 0, 'errmsg': 'ok', 'data': data}


@rest_resource
class DeviceChat(BaseResource):
    endpoints = ['/device/chat']

    def __init__(self):
        self.iot_server = IotServer.get_instance()

    def get(self):
        return request.args

    def post(self):
        ret = self.iot_server.send_device_message(request.json.get('data'))
        if ret:
            return {'errcode': 0, 'errmsg': 'ok'}
        else:
            return {'errcode': -1, 'errmsg': 'failed'}


@rest_resource
class DeviceChatListen(BaseResource):
    endpoints = ['/device/chat/listen']

    def get(self):
        """
        读取聊天信息
        :return:
        """
        with open(APP_PATH + '/data/client_report_data.json', mode='r+') as f:
            read_str = f.read().strip()
            if read_str:
                data = json.loads(read_str)
            else:
                return {'errcode': 0, 'errmsg': 'ok', 'data': False}
        with open(APP_PATH + '/data/client_report_data.json', mode='w') as f:
            f.write('')
        return {'errcode': 0, 'errmsg': 'ok', 'data': data}

    def post(self):
        """
        接受设备推送的反馈
        :return:
        """
        ret = request.json.get('data')
        if isinstance(ret, dict):
            ret = json.dumps(ret)
        with open(APP_PATH + '/data/client_report_data.json', mode='w+') as f:
            f.write(ret)
            return {'errcode': 0, 'errmsg': 'ok'}



@rest_resource
class SecureResourceOne(SecureResource):
    """ /api/resource/two """
    endpoints = ['/resource/two/<string:resource_id>']

    def get(self, resource_id):
        return {'name': 'Resource Two', 'data': resource_id}

