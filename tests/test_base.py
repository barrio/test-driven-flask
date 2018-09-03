from flask import current_app, session


def test_app_exists(appl):
    assert current_app


def test_app_is_testing(appl):
    assert current_app.config['TESTING']


def test_index_page_is_rendered(client):
    response = client.get('/')
    assert 'OK' in response.status
    assert b'Test-driven Flask' in response.data


def test_form_submit(client):
    response = client.post('/', data={'name': 'Marco'}, follow_redirects=True)
    assert 'OK' in response.status
    assert b'Marco' in response.data


def test_session(client):
    with client:  # Keep request context to access session
        response = client.post('/', data={'name': 'Marco'}, follow_redirects=True)
        assert 'OK' in response.status
        assert session['name'] == 'Marco'


def test_flash_message(client):
    response = client.post('/', data={'name': 'Julian'}, follow_redirects=True)
    assert 'OK' in response.status
    assert b"You changed your name!" not in response.data

    response = client.post('/', data={'name': 'Marco'}, follow_redirects=True)
    assert 'OK' in response.status
    assert b"You changed your name!" in response.data


