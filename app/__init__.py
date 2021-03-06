from flask import Flask
from flask_bootstrap import Bootstrap
from config import config

bootstrap = Bootstrap()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    bootstrap.init_app(app)
    if app.config['SSL_REDIRECT']:
        from flask_talisman import Talisman
        csp = {
            'default-src': [
                '\'self\'',
                'cdnjs.cloudflare.com'
                ]
        }
        Talisman(app, content_security_policy = csp)

    from .main import main
    app.register_blueprint(main)

    return app
