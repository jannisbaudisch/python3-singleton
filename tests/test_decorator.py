import pytest
from singleton.decorator import singleton


class Mock:
    def __init__(self):
        pass

    def add(self, a, b):
        return a + b


MockSingleton = singleton(Mock)


def test_constructor_returns_a_working_instance():
    instance = MockSingleton()
    assert isinstance(instance, Mock)
    assert instance.add(1, 2) == 3


def test_constructor_returns_same_instance():
    instance_1 = MockSingleton()
    instance_2 = MockSingleton()

    assert instance_1 == instance_2


def test_test_mode():
    singleton_instance = MockSingleton()
    singleton.testing()
    instance_1 = MockSingleton()
    instance_2 = MockSingleton()
    assert singleton_instance != instance_1 and singleton_instance != instance_2
    assert instance_1 != instance_2


def test_test_mode_disabling():
    singleton_instance = MockSingleton()
    singleton.testing(True)
    singleton.testing(False)
    instance_1 = MockSingleton()
    instance_2 = MockSingleton()
    assert singleton_instance != instance_1 and singleton_instance != instance_2
    assert instance_1 == instance_2


def test_constructor_arguments_throw_error():
    class MockWithConstructorArguments:
        def __init__(self, a, b):
            pass

    with pytest.raises(KeyError):
        singleton(MockWithConstructorArguments)
