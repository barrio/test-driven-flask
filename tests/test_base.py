from flask import current_app, request


def test_app_exists(client):
    assert current_app


def test_app_is_testing(client):
    assert current_app.config['TESTING']


def test_index_page_is_rendered(client):
    response = client.get('/')

    assert response.status_code == 200
    assert b'Test-driven Flask' in response.data


def test_form_submit(client):
    response = client.post('/', data={'name': 'Marco'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Marco' in response.data
