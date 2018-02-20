from flask import Flask

from app.api import api_rest, api_bp
from app.client import client_bp
from app.components.iot_shadow_cfg import refresh_shadow_cfg_cache

app = Flask(__name__, static_url_path='')
app.register_blueprint(api_bp)
app.register_blueprint(client_bp)
print(refresh_shadow_cfg_cache())

from . import config
app.logger.info('>>> {}'.format(app.config['MODE']))

