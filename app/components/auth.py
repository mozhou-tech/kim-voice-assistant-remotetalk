from app.components.iot_shadow_cfg import get_shadow_cfg


def check_passwd(input_passwd):
    """
    检查密码是否正确
    :return:
    """
    shadow_dict = get_shadow_cfg()
    return shadow_dict['cfg_remote_control_password'] == input_passwd
