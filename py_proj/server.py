"""

    py_proj.server
    ~~~~~~~~~~~~~~

    Модуль серверных приложений.

"""

import sys

from gunicorn.app.base import Application


class FlaskGunicornApplication(Application):
    """Gunicorn-приложение для py_proj."""

    def __init__(self, app, config, *args, **kwargs):
        #: Flask-приложение
        self.app = app
        #: Словарь настроек приложения
        self.config = config
        # Предотвращаем передачу аргументов команды в приложение
        sys.argv = [sys.argv[0]]
        super(FlaskGunicornApplication, self).__init__(*args, **kwargs)

    def init(self, parser, opts, args):
        """Инициализирует конфигурацию приложения.
        Метод переопределяет родительский для использования конфигурации,
        с которой было инициализировано приложение.
        :param parser: Объект argparse.ArgumentParser конфигурации.
        :param opts: Опции командной строки.
        :param args: Аргументы командной строки.
        """
        return self.config

    def load(self):
        """Загружает приложение.
        Метод переопределяет родительский для возврата Flask-приложения,
        с которым было инициализировано приложение.
        """
        return self.app
