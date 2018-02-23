from flask import Flask

from app.api import api_rest, api_bp
from app.client import client_bp
from app.components.iot_shadow_cfg import read_shadow_cfg_from_cache

app = Flask(__name__, static_url_path='')
app.register_blueprint(api_bp)
app.register_blueprint(client_bp)
read_shadow_cfg_from_cache(refresh=True)

from . import config
app.logger.info('>>> {}'.format(app.config['MODE']))

