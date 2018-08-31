from flask import current_app


def test_app_exists(client):
    assert current_app


def test_app_is_testing(client):
    assert current_app.config['TESTING']


def test_index_page_is_rendered(client):
    index = client.get('/')

    assert index.status_code == 200
    assert b'Test-driven Flask' in index.data
