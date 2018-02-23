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
import json, time
from app.components.auth import check_passwd, check_api_token
from app.components.iot_shadow_cfg import read_shadow_cfg_from_cache


@rest_resource
class Auth(BaseResource):
    endpoints = ['/auth']

    def __init__(self):
        pass

    def post(self):
        read_shadow_cfg_from_cache(True)
        time.sleep(0.5)

        if check_passwd(request.get_json()['passwd']):
            return {'errcode': 0, 'errmsg': 'ok', 'data': {
                'api_token': read_shadow_cfg_from_cache()['cfg_remote_control_api_token']
            }}
        else:
            return {'errcode': -1, 'errmsg': 'Auth error, check your password.'}


@rest_resource
class DeviceLog(BaseResource):
    """ /api/resource/one """
    endpoints = ['/device/log']

    def __init__(self):
        self.ots_client = OTSTools.get_instance()

    def get(self):
        if not 'token' in request.args.keys() or not check_api_token(request.args['token']):
            return {'errcode': -1, 'errmsg': 'wrong api token.'}

        return self.ots_client.get_last_limit_row()


@rest_resource
class DeviceStat(BaseResource):
    """ /api/resource/one """
    endpoints = ['/device/stat']

    def __init__(self):
        self.iot_server = IotServer.get_instance()

    def get(self):
        if not 'token' in request.args.keys() or not check_api_token(request.args['token']):
            return {'errcode': -1, 'errmsg': 'wrong api token.'}

        data = self.iot_server.get_device_stat()
        data = dict(read_shadow_cfg_from_cache().items() | data.items())
        del data['cfg_remote_control_password']
        del data['cfg_remote_control_api_token']
        return {'errcode': 0, 'errmsg': 'ok', 'data': data}


@rest_resource
class DeviceChat(BaseResource):
    endpoints = ['/device/chat']

    def __init__(self):
        self.iot_server = IotServer.get_instance()

    def post(self):
        if not 'token' in request.args.keys() or not check_api_token(request.args['token']):
            return {'errcode': -1, 'errmsg': 'wrong api token.'}

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
        if not 'token' in request.args.keys() or not check_api_token(request.args['token']):
            return {'errcode': -1, 'errmsg': 'wrong api token.'}

        args = request.args
        # logs = ''
        logs = self.ots_client.get_last_limit_row_by_timestamp(start_timestamp=int(args['timestamp']))
        return {'errcode': 0, 'errmsg': 'ok', 'data': {'args': args, 'logs': logs}}

