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

    def test_batch_get_row(self):
        """
        批量读取行数据
        :return:
        """
        self.ots_client.batch_get_row()



if __name__ == '__main__':
    logger.init(info=True)
    unittest.main()

