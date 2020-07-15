import pytest
from singleton.decorator import singleton


@pytest.fixture
def isolate_singleton():
    testing = singleton._testing
    singleton.testing(False)
    yield singleton
    singleton.testing(testing)

@pytest.fixture
def disable_singleton():
    testing = singleton._testing
    singleton.testing(True)
    yield singleton
    singleton.testing(testing)