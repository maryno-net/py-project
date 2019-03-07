import pytest

from py_proj.app import create_app
from py_proj.settings import TestConfig


@pytest.fixture
def app(tmpdir):
    """Фикстура текущего Flask-приложения."""
    TestConfig.UPLOAD_FOLDER = str(tmpdir)
    app = create_app(TestConfig)
    return app
