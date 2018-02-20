from config.path import IOT_SHADOW_PATH
import json
from app.components.aliyun_iot import IotServer


def read_shadow_cfg_from_cache():
    """
    从文件缓存中获取
    :return:
    """
    with open(IOT_SHADOW_PATH, mode='r') as f:
        return json.loads(f.read())['state']['reported']


def refresh_shadow_cfg_cache():
    """
    刷新配置缓存
    :return:
    """
    return IotServer.get_instance().get_iot_shadow()