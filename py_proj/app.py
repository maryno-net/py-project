"""

    py_proj.app
    ~~~~~~~~~~~

    Flask-приложение py-proj.

"""

from flask import Flask
from werkzeug.contrib.fixers import ProxyFix

from py_proj.errorhandlers import api_error, fatal, forbidden, not_found
from py_proj.example.views import example
from py_proj.exceptions import APIError


def create_app(config_object):
    """Фабрика"""
    app = Flask(__name__)
    app.config.from_object(config_object)
    app.wsgi_app = ProxyFix(app.wsgi_app)
    register_extensions(app)
    register_blueprints(app)
    register_errorhandlers(app)
    return app


def register_extensions(app):
    """Зарегистрировать расширения для Flask-приложения.

    :param app: Flask-приложение.
    """
    return None


def register_blueprints(app):
    """Зарегистрировать blueprint'ы Flask-приложения.

    :param app: Flask-приложение.
    """
    app.register_blueprint(example, url_prefix='/api')
    return None


def register_errorhandlers(app):
    """Зарегистрировать специальные обработчки ошибок для Flask-приложения.

    :param app: Flask-приложение.
    """
    app.errorhandler(403)(forbidden)
    app.errorhandler(404)(not_found)
    app.errorhandler(500)(fatal)
    app.errorhandler(APIError)(api_error)
