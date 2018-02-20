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
from app.components.auth import check_passwd
from app.components.iot_shadow_cfg import get_shadow_cfg


@rest_resource
class Auth(BaseResource):
    endpoints = ['/auth']

    def __init__(self):
        pass

    def post(self):
        if check_passwd(request.get_json()['passwd']):
            return {'errcode': 0, 'errmsg': 'ok'}
        else:
            return {'errcode': -1, 'errmsg': 'Auth error, check your password.'}


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
        data = dict(get_shadow_cfg().items() | data.items())
        del data['cfg_remote_control_password']
        del data['cfg_remote_control_api_token']
        return {'errcode': 0, 'errmsg': 'ok', 'data': data}


@rest_resource
class DeviceChat(BaseResource):
    endpoints = ['/device/chat']

    def __init__(self):
        self.iot_server = IotServer.get_instance()

    def get(self):
        return request.args

    def post(self):
        ret = self.iot_server.send_device_message(request.get_json()['data'])
        if ret:
            return {'errcode': 0, 'errmsg': 'ok'}
        else:
            return {'errcode': -1, 'errmsg': 'failed'}


@rest_resource
class DeviceChatListen(BaseResource):
    endpoints = ['/device/chat/listen']

    def __init__(self):
        self.ots_client = OTSTools.get_instance()

    def get(self):
        """
        读取聊天信息
        :return:
        """
        args = request.args
        # logs = ''
        logs = self.ots_client.get_last_limit_row_by_timestamp(start_timestamp=int(args['timestamp']))
        return {'errcode': 0, 'errmsg': 'ok', 'data': {'args': args, 'logs': logs}}

