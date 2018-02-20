# -*- coding: utf-8-*-
import unittest
import os
os.sys.path.append(os.path.join(os.path.dirname(__file__), '../'))
from app.components import logger
from app.components.aliyun_iot import IotServer


class TestComponentsAliyunIOT(unittest.TestCase):
    """
    表格计算
    """

    def setUp(self):
        self.iot_server = IotServer.get_instance()

    def test_send_device_message(self):
        """
        批量读取行数据
        :return:
        """
        self.iot_server.send_device_message('马云')

    def test_sync_iot_shadow(self):
        r = self.iot_server.get_iot_shadow()
        print(r)
        pass


if __name__ == '__main__':
    logger.init(info=True)
    unittest.main()

