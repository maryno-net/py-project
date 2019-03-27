"""

    py_proj.settings
    ~~~~~~~~~~~~~~~~

    Настройки py_proj.

"""

import os


class Config:
    SECRET_KEY = 'SecretKeyForSessionSigning'
    APP_DIR = os.path.abspath(os.path.dirname(__file__))  # This directory
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
    JSONIFY_PRETTYPRINT_REGULAR = False


class TestConfig(Config):
    pass
