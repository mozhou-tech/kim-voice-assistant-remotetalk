import config
yaml_settings = config.load_yaml_settings()

aliyun_ak_id = yaml_settings['aliyun']['ak_id']
aliyun_ak_secret = yaml_settings['aliyun']['ak_secret']
aliyun_ots_endpoint = yaml_settings['aliyun']['tablestore']['endpoint']
aliyun_ots_instance = yaml_settings['aliyun']['tablestore']['instance_name']
aliyun_ots_conversation_table = yaml_settings['aliyun']['tablestore']['conversation_table_name']
aliyun_iot_device_name = yaml_settings['aliyun']['iothub']['device_name']
aliyun_iot_product_key = yaml_settings['aliyun']['iothub']['product_key']