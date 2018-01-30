from tablestore import *
from config import profile
import time
import json


class OTSTools:
    def __init__(self):
        self.client = OTSClient(end_point=profile.aliyun_endpoint, access_key_id=profile.aliyun_ak_id,
                                access_key_secret=profile.aliyun_ak_secret, instance_name='xy-conversations')
        self.table_name = 'conversation_logs'

    def get_table_list(self):
        tables = self.client.list_table()
        print(tables)

    def batch_get_row(self, start_timestamp=INF_MAX, end_timestamp=INF_MIN, limit=10):
        inclusive_start_primary_key = [('device', 'xiaoyun001'), ('timestamp', start_timestamp)]
        exclusive_end_primary_key = [('device', 'xiaoyun001'), ('timestamp', end_timestamp)]
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

        for row in all_rows:
            print(row.primary_key, row.attribute_columns)
        print('Total rows: ', len(all_rows))

    def __del__(self):
        pass

    @classmethod
    def get_instance(cls):
        return OTSTools()


    