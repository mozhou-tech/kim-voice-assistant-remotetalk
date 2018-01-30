import tablestore
from config import profile


class OTSClient:
    def __init__(self):
        self.client = tablestore.OTSClient(end_point=profile.aliyun_endpoint, access_key_id=profile.aliyun_ak_id,
                                           access_key_secret=profile.aliyun_ak_secret,instance_name='xy-conversations')

    def get_table_list(self):
        print('Begin ListTable')
        tables = self.client.list_table()
        print('All the tables you have created:')
        for table in tables:
            print(table)
        print('End ListTable')

    def __del__(self):
        pass

    @classmethod
    def get_instance(cls):
        return OTSClient()


    