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

    def test_get_hour_row(self):
        """
        批量读取行数据
        :return:
        """


if __name__ == '__main__':
    logger.init(info=True)
    unittest.main()

