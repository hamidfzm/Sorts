__author__ = 'hamid'

# import flask
from flask import Flask
from flask.ext.bootstrap import Bootstrap
from config import DevelopmentConfig


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    app.template_folder = '../templates'
    app.static_folder = '../static'

    Bootstrap(app)

    # blueprint with error handlers
    @app.errorhandler(404)
    def page_not_found(e):
        return '404 - Page Not Found', 404

    @app.errorhandler(500)
    def internal_server_error(e):
        return '500 - Internal Server Error', 500

    # attach routes and custom error pages here
    return app


app = create_app(DevelopmentConfig)
from app.views import *