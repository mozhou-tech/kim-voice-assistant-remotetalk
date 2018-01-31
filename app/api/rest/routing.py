"""
REST API Resource Routing

http://flask-restful.readthedocs.io/en/latest/
"""

import time
from flask import request
from app.api.rest.base import BaseResource, SecureResource, rest_resource
from app.components.aliyun_ots import OTSTools


@rest_resource
class DeviceLog(BaseResource):
    """ /api/resource/one """
    endpoints = ['/device/log']

    def __init__(self):
        self.ots_client = OTSTools.get_instance()

    def get(self):
        return self.ots_client.get_last_limit_row()



@rest_resource
class DeviceChat(BaseResource):
    endpoints = ['/device/chat']

    def get(self, *args, **kwargs):
        return kwargs

    def post(self, *args, **kwargs):
        return ['asdf']


@rest_resource
class SecureResourceOne(SecureResource):
    """ /api/resource/two """
    endpoints = ['/resource/two/<string:resource_id>']

    def get(self, resource_id):
        return {'name': 'Resource Two', 'data': resource_id}

