import pytest

from app import create_app


@pytest.fixture(scope='module')
def client():
    app = create_app('testing')

    client = app.test_client()
    context = app.app_context()
    context.push()

    yield client
    context.pop()
