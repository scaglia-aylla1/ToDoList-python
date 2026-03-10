from flask import Flask
from config import Config
from .extensions import db, migrate, api


def create_app(test_config=None):
    app = Flask(__name__)

    app.config.update({
        "API_TITLE": "Todo List API",
        "API_VERSION": "v1",
        "OPENAPI_VERSION": "3.0.3",
        "OPENAPI_URL_PREFIX": "/docs",
        "OPENAPI_SWAGGER_UI_PATH": "/swagger",
        "OPENAPI_SWAGGER_UI_URL": "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    })
    
    if test_config:
        app.config.update(test_config)
    else:
        app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    api.init_app(app)

    from .routes import blp
    api.register_blueprint(blp)

    return app