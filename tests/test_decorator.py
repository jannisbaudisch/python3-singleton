from singleton.decorator import singleton
from singleton.decorator.pytest import enable_singleton


class Mock:
    def add(self, a, b):
        return a + b


SingleMock = singleton(Mock)


def test_constructor_returns_an_instance(enable_singleton):
    instance = SingleMock()
    assert instance.add(1, 2) == 3


def test_constructor_returns_same_instance(enable_singleton):
    instance_1 = SingleMock()
    instance_2 = SingleMock()

    assert instance_1 == instance_2


def test_constructor_returns_new_instance_in_test_mode(enable_singleton):
    singleton.testing()
    instance_1 = SingleMock()
    instance_2 = SingleMock()
    assert instance_1 != instance_2
