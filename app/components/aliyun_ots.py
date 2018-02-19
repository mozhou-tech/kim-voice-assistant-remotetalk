from tablestore import *
from config import profile
import time
import json
import logging


class OTSTools:
    def __init__(self):
        self.client = OTSClient(end_point=profile.aliyun_ots_endpoint, access_key_id=profile.aliyun_ak_id,
                                access_key_secret=profile.aliyun_ak_secret, instance_name=profile.aliyun_ots_instance)
        self.table_name = profile.aliyun_ots_conversation_table
        self.logger = logging.getLogger()

    def get_table_list(self):
        """
        获取表格列表
        :return:
        """
        tables = self.client.list_table()
        print(tables)

    def get_last_limit_row_by_timestamp(self, start_timestamp=None, device=profile.aliyun_iot_device_name, limit=10):
        """
        根据时间戳获取一段时间的会话日志
        :return:
        """
        if start_timestamp == 0:
            return []
        if len(str(start_timestamp)) != 13:
            self.logger.error('timestamp应该有13位长')

        self.logger.info('read last conversation logs from tablestore.')
        inclusive_start_primary_key = [('device', device), ('timestamp', start_timestamp)]
        exclusive_end_primary_key = [('device', device), ('timestamp', INF_MAX)]
        columns_to_get = []

        consumed, next_start_primary_key, row_list, next_token = self.client.get_range(
            self.table_name, Direction.FORWARD,
            inclusive_start_primary_key, exclusive_end_primary_key,
            columns_to_get,
            limit,
            column_filter=None,
            max_version=1
        )
        return self._row_data_to_dict(row_list)

    def _row_data_to_dict(self, row_list):
        """
        表格计算返回的原始数据转换为Dict存储
        :return:
        """
        data_dict_arr = []
        for row in row_list:
            data_dict_holder = {}
            for item in row.primary_key:
                data_dict_holder[item[0]] = item[1]
            for item in row.attribute_columns:
                data_dict_holder[item[0]] = item[1]
            data_dict_arr.append(data_dict_holder)
        return data_dict_arr

    def get_last_limit_row(self, device=profile.aliyun_iot_device_name, limit=60):
        """
        获取最近的N条日志
        :return:
        """
        self.logger.info('read last conversation logs from tablestore.')
        inclusive_start_primary_key = [('device', device), ('timestamp', INF_MAX)]
        exclusive_end_primary_key = [('device', device), ('timestamp', INF_MIN)]
        columns_to_get = []

        consumed, next_start_primary_key, row_list, next_token = self.client.get_range(
            self.table_name, Direction.BACKWARD,
            inclusive_start_primary_key, exclusive_end_primary_key,
            columns_to_get,
            limit,
            column_filter=None,
            max_version=1
        )
        return self._row_data_to_dict(row_list)

    def get_hour_row(self, device=profile.aliyun_iot_device_name, start_timestamp=INF_MAX, limit=60):
        """
        获取某个时间点，往前推一个小时内的所有日志
        :param device:
        :param start_timestamp:
        :param limit:
        :return:
        """
        self.logger.info('hourly read conversation logs from tablestore.')
        end_timestamp = int(time.time() - 60 * 60) * 1000
        inclusive_start_primary_key = [('device', device), ('timestamp', start_timestamp)]
        exclusive_end_primary_key = [('device', device), ('timestamp', end_timestamp)]
        columns_to_get = []

        consumed, next_start_primary_key, row_list, next_token = self.client.get_range(
            self.table_name, Direction.BACKWARD,
            inclusive_start_primary_key, exclusive_end_primary_key,
            columns_to_get,
            limit,
            column_filter=None,
            max_version=1
        )
        all_rows = []
        all_rows.extend(row_list)
        while next_start_primary_key is not None:
            inclusive_start_primary_key = next_start_primary_key
            consumed, next_start_primary_key, row_list, next_token = self.client.get_range(
                self.table_name, Direction.BACKWARD,
                inclusive_start_primary_key, exclusive_end_primary_key,
                columns_to_get, limit,
                column_filter=None,
                max_version=1
            )
            all_rows.extend(row_list)
        return self._row_data_to_dict(all_rows)

    def __del__(self):
        pass

    @classmethod
    def get_instance(cls):
        return OTSTools()


    