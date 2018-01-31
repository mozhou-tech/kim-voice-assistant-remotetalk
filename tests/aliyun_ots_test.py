# -*- coding: utf-8-*-
import unittest
import os
os.sys.path.append(os.path.join(os.path.dirname(__file__), '../'))
from app.components import logger
from app.components.aliyun_ots import OTSTools


class TestComponentsAliyunOTS(unittest.TestCase):
    """
    表格计算
    """

    def setUp(self):
        self.ots_client = OTSTools.get_instance()

    def atest_table_list(self):
        """
        列出所有表格
        :return:
        """
        self.ots_client.get_table_list()

    def atest_get_last_limit_row(self):
        """
        获得
        :return:
        """
        print(self.ots_client.get_last_limit_row())

    def test_get_hour_row(self):
        """
        批量读取行数据
        :return:
        """
        print(self.ots_client.get_hour_row())


if __name__ == '__main__':
    logger.init(info=True)
    unittest.main()

