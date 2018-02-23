from config.path import IOT_SHADOW_PATH
import json,time
from app.components.aliyun_iot import IotServer


def read_shadow_cfg_from_cache(refresh=False):
    """
    从文件缓存中获取
    :return:
    """
    if refresh:
        IotServer.get_instance().get_iot_shadow()
    else:
        try:
            f = open(IOT_SHADOW_PATH, mode='r')
            file_data = f.read()
            return json.loads(file_data)['state']['reported']
        except:
            read_shadow_cfg_from_cache(True)
            raise Exception('read shadow cfg error, please try again.')



