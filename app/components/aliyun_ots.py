from tablestore import *
from config import profile
import time


class OTSTools:
    def __init__(self):
        self.client = OTSClient(end_point=profile.aliyun_endpoint, access_key_id=profile.aliyun_ak_id,
                                access_key_secret=profile.aliyun_ak_secret, instance_name='xy-conversations')
        self.table_name = 'conversation_logs'

    def get_table_list(self):
        tables = self.client.list_table()
        print(tables)

    def batch_get_row(self):
        inclusive_start_primary_key = [('device', 'xiaoyun001'), ('timestamp', INF_MAX)]
        exclusive_end_primary_key = [('device', 'xiaoyun001'), ('timestamp', INF_MIN)]
        columns_to_get = []
        limit = 90

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

        for row in all_rows:
            print(row.primary_key, row.attribute_columns)

    def __del__(self):
        pass

    @classmethod
    def get_instance(cls):
        return OTSTools()


    