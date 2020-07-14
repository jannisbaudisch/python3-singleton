import pytest
from singleton.decorator import singleton


@pytest.fixture
def enable_singleton():
    singleton._testing = False
    singleton._instance = None
    yield singleton
    singleton.testing()


