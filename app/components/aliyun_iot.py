
from aliyunsdkcore import client
from aliyunsdkiot.request.v20170420 import RegistDeviceRequest
from aliyunsdkiot.request.v20170420 import PubRequest, UpdateDeviceShadowRequest
from config import profile
import logging, json, base64


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
        if isinstance(payload, str):
            payload = payload.encode('utf8')

        self.clt = client.AcsClient(self.accessKeyId, self.accessKeySecret, 'cn-shanghai')
        self.request = PubRequest.PubRequest()
        self.request.set_accept_format('json')  # 设置返回数据格式
        self.request.set_ProductKey(profile.aliyun_iot_product_key)

        full_topic = '/'+profile.aliyun_iot_product_key+'/'+profile.aliyun_iot_device_name + '/get_mic_text_from_server'
        self.request.set_TopicFullName(full_topic)  # 消息发送到的Topic全名
        self.request.set_MessageContent(base64.b64encode(payload).decode('utf8'))  # hello world Base64 String
        self.request.set_Qos(1)
        # print(self.request)
        result = json.loads(self.clt.do_action_with_exception(self.request).decode('utf8'))
        return result['Success']

    @classmethod
    def get_instance(cls):
        return IotServer()
