from flask import session
import pytest

from app import create_app


@pytest.fixture(scope='module')
def appl():
    appl = create_app('testing')
    context = appl.app_context()
    context.push()

    yield appl
    context.pop()


@pytest.fixture(scope='module')
def client(appl):
    client = appl.test_client()
    yield client
