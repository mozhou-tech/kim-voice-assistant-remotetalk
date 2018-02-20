from app.components.iot_shadow_cfg import read_shadow_cfg_from_cache
shadow_dict = read_shadow_cfg_from_cache()


def check_passwd(input_passwd):
    """
    检查密码是否正确
    :return:
    """
    return shadow_dict['cfg_remote_control_password'] == input_passwd


def check_api_token(input_token):
    """
    检查api token是否正确
    :return:
    """
    return shadow_dict['cfg_remote_control_api_token'] == str(input_token)
