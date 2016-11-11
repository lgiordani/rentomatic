import pytest


from rentomatic.app import create_app
from rentomatic.settings import TestConfig


@pytest.yield_fixture(scope='function')
def app():
    return create_app(TestConfig)
