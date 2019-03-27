"""

    py_proj.cli
    ~~~~~~~~~~~

    Интерфейс командной строки.

"""

import logging
import multiprocessing

import click

from py_proj import __version__
from py_proj.app import create_app
from py_proj.server import FlaskGunicornApplication
from py_proj.settings import Config

WORKERS = multiprocessing.cpu_count() * 2 + 1

LOG_LEVEL_CHOICE = click.Choice(logging._nameToLevel)


def init_app():
    """Инициализировать Flask-приложение."""
    config_object = Config
    app = create_app(config_object)
    return app


def show_version(ctx, param, value):
    """Отобразить версию приложения и завершить работу.
    Используется в качестве callback'а в опции --version.
    :param click.Context ctx: Объект контекста.
    :param click.Parameter param: Объект параметра.
    :param value: Значение параметра.
    """
    if value and not ctx.resilient_parsing:
        version = "py_proj {}".format(__version__)
        click.echo(version, color=ctx.color)
        ctx.exit()


def show_help(ctx, param, value):
    """Отобразить это справочное сообщение и завершить работу.
    Используется в качестве callback'а в опции --help.
    :param click.Context ctx: Объект контекста.
    :param click.Parameter param: Объект параметра.
    :param value: Значение параметра.
    """
    if value and not ctx.resilient_parsing:
        click.echo(ctx.get_help(), color=ctx.color)
        ctx.exit()


# Опция для отображения справочной информации
help_option = click.option(
    "-h", "--help", is_flag=True, callback=show_help, expose_value=False,
    is_eager=True, help="Отобразить эту справочную информацию и "
    "завершить работу")


@click.group()
@click.option("-v", "--version", is_flag=True, callback=show_version,
              expose_value=False, is_eager=True,
              help="Отобразить версию приложения и завершить работу")
@help_option
def cli():
    """Интерфейс командной строки для Flask-приложения"""
    pass


@cli.group()
@click.pass_context
@help_option
def server(ctx):
    """Запустить сервер Gunicorn"""
    ctx.obj = init_app()


@server.command()
@click.pass_obj
@click.option("-b", "--bind", default="127.0.0.1:9000",
              help="Сокет для привязки")
@click.option("-w", "--workers", type=click.IntRange(min=1), default=WORKERS,
              help="Количество воркеров для обработки запросов")
@click.option("--log-level", type=LOG_LEVEL_CHOICE, default="INFO",
              help="Уровень выводимых логов")
@help_option
def start(app, bind, workers, log_level):
    """Запустить сервер Gunicorn"""
    config = {
        "bind": bind,
        "workers": workers,
        "worker_class": "gthread",
        "loglevel": log_level,
    }
    gunicorn = FlaskGunicornApplication(app=app, config=config)
    gunicorn.run()
