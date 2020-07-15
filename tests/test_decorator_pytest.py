from singleton.decorator.pytest import singleton, isolate_singleton, disable_singleton


@singleton
class Mock:
    value = 0


def test_setup_isolate_test():
    singleton.testing(False)
    mock = Mock()
    mock.value = 1
    assert mock.value == 1
    assert singleton._testing == False


def test_isolate_fixture(isolate_singleton):
    mock1 = Mock()
    mock2 = Mock()
    assert mock1.value == 0
    assert mock2.value == 0
    assert mock1 == mock2

    mock1.value = 1


def test_isolate_fixture_reset_singleton_afterwards():
    mock = Mock()
    assert mock.value == 0
    assert singleton._testing == False


def test_setup_disable_test():
    singleton.testing(False)
    mock = Mock()
    mock.value = 1
    assert mock.value == 1
    assert singleton._testing == False


def test_disable_fixture(disable_singleton):
    mock1 = Mock()
    mock2 = Mock()
    assert mock1.value == 0
    assert mock2.value == 0
    assert mock1 != mock2

    mock1.value = 1


def test_disable_fixture_reset_singleton_afterwards():
    mock = Mock()
    assert mock.value == 0
    assert singleton._testing == False


def test_setup_set_testing_back_to_old_value_isolate_fixture():
    singleton.testing(True)


def test_set_testing_back_to_old_value_isolate_fixture(isolate_singleton):
    pass


def test_got_testing_set_back_to_old_value_for_isolate_fixture():
    assert singleton._testing == True


def test_setup_set_testing_back_to_old_value_disable_fixture():
    singleton.testing(True)


def test_set_testing_back_to_old_value_disable_fixture(disable_singleton):
    pass


def test_got_testing_set_back_to_old_value_for_disable_fixture():
    assert singleton._testing == True
