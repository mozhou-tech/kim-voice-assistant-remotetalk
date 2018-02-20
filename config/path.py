import os

APP_PATH = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir))

LOG_PATH = APP_PATH + '/data/service.log'

IOT_SHADOW_PATH = APP_PATH + '/data/iot_shadow.json'
