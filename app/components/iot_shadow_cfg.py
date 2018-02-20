from config.path import IOT_SHADOW_PATH
import json


def get_shadow_cfg():
    with open(IOT_SHADOW_PATH, mode='r') as f:
        return json.loads(f.read())['state']['reported']