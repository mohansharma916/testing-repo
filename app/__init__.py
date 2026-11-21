"""STAF SAST demo application - deliberately vulnerable. Do not deploy."""
from flask import Flask

from . import (admin, auth, client, config, data_service, files, login,
               net_tools, reset, session, store, upload, webhooks)

BLUEPRINTS = (admin, auth, client, data_service, files, login, net_tools,
              reset, session, upload, webhooks)


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = config.SECRET_KEY
    store.init()
    for module in BLUEPRINTS:
        app.register_blueprint(module.bp)
    return app
