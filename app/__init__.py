from flask import Flask

from app.api import api_rest, api_bp
from app.client import client_bp
from app.components.aliyun_iot import IotServer

app = Flask(__name__, static_url_path='')
app.register_blueprint(api_bp)
app.register_blueprint(client_bp)
IotServer.get_instance().get_iot_shadow()

from . import config
app.logger.info('>>> {}'.format(app.config['MODE']))

