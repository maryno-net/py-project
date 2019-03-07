"""

    py_proj.exceptions
    ~~~~~~~~~~~~~~~~~~~

    Исключения специфические для системы py_proj.

"""


class APIError(Exception):
    """Исключение при обработке запроса."""

    #: Код статуса, возвращаемого клиенту по умолчанию.
    _default_status_code = 400

    def __init__(self, message, status_code=None):
        Exception.__init__(self)
        #: Сообщение об ошибке
        self.message = message
        #: Код статуса, возвращаемого клиенту
        if status_code is None:
            self.status_code = self._default_status_code
        else:
            self.status_code = status_code
