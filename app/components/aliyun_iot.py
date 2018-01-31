from aliyunsdkcore import client
from aliyunsdkiot.request.v20170420 import RegistDeviceRequest
from aliyunsdkiot.request.v20170420 import PubRequest,UpdateDeviceShadowRequest
from config import profile, device
import logging, json,base64


class IotServer:

    def __init__(self):
        """
        初始化
        """
        self.accessKeyId = profile.aliyun_ak_id
        self.accessKeySecret = profile.aliyun_ak_secret
        self._logger = logging.getLogger()

    def send_device_message(self, payload):
        """
        发送设备消息
        :return:
        """



    @classmethod
    def get_instance(cls):
        return IotServer()
