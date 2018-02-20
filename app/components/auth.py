from config.path import IOT_SHADOW_PATH
import json


def check_passwd(input_passwd):
    """
    检查密码是否正确
    :return:
    """
    with open(IOT_SHADOW_PATH, mode='r') as f:
        shadow_dict = json.loads(f.read())
    return shadow_dict['state']['reported']['passwd'] == input_passwd
