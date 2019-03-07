import random

from flask import url_for


class TestExampleViews:
    """Тесты для примера."""

    def test_get_example_json(self, client):
        """/api/example/:some_id (GET) возвращает :some_id."""
        some_id = random.randint(1, 1000)
        url = url_for('example.get_example_json', some_id=some_id)
        response = client.get(url)
        assert response.status == '200 OK'
        assert response.json['some_id'] == some_id
