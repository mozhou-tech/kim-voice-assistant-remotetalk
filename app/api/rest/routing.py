"""
REST API Resource Routing

http://flask-restful.readthedocs.io/en/latest/
"""

import time
from flask import request
from app.api.rest.base import BaseResource, SecureResource, rest_resource


@rest_resource
class DeviceLog(BaseResource):
    """ /api/resource/one """
    endpoints = ['/device/log']

    def get(self):
        return {'device_name': 'xiaoyun', 'log_content': True, 'datetime' : '2018-01-28 21:00:03'}

    def post(self):
        json_payload = request.json
        return {'name': 'Resource Post'}


@rest_resource
class DeviceChat(BaseResource):
    endpoints = ['/device/chat']

    def get(self, *args, **kwargs):
        return {}



@rest_resource
class SecureResourceOne(SecureResource):
    """ /api/resource/two """
    endpoints = ['/resource/two/<string:resource_id>']

    def get(self, resource_id):
        return {'name': 'Resource Two', 'data': resource_id}

