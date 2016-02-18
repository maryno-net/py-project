"""

    py_proj.errorhandlers
    ~~~~~~~~~~~~~~~~~~~~~

    Обработчики HTTP ответов со статусами 4XX и 5XX, а также ошибок типа
    APIError.

"""

from flask import current_app, jsonify, request


def forbidden(error=None):
    """Обработчик ошибки 403."""
    message = 'Access denied: {}'.format(request.url)
    current_app.logger.error(message)
    response = jsonify({'message': message, 'status': 'forbidden'})
    response.status_code = 403
    return response


def not_found(error=None):
    """Обработчик ошибки 404."""
    message = 'Not Found: {}'.format(request.url)
    current_app.logger.error(message)
    response = jsonify({'message': message, 'status': 'error'})
    response.status_code = 404
    return response


def fatal(exception):
    """Обработчик ошибки 500."""
    message = 'Server Error: {}'.format(request.url)
    current_app.logger.exception(exception)
    response = jsonify({'message': message, 'status': 'error'})
    response.status_code = 500
    return response


def api_error(exception):
    """Обработчик ошибки APIError."""
    current_app.logger.exception(exception)
    response = jsonify({'message': exception.message, 'status': 'error'})
    response.status_code = exception.status_code
    return response
