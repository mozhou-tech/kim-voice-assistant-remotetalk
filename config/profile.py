import config
yaml_settings = config.load_yaml_settings()

aliyun_ak_id = yaml_settings['aliyun']['ak_id']
aliyun_ak_secret = yaml_settings['aliyun']['ak_secret']
aliyun_endpoint = yaml_settings['aliyun']['ots_endpoint']
