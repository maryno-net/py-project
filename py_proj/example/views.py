"""

    py_proj.example.views
    ~~~~~~~~~~~~~~~~~~~~~

    Точки API для примера.

"""
from flask import Blueprint, jsonify

example = Blueprint('example', __name__)


@example.route('/example/<int:some_id>', methods=['GET'])
def get_example_json(some_id):
    """/example/:some_id (GET) Получить some_id."""
    return jsonify({'some_id': some_id}), 200
