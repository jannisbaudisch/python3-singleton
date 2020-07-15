import inspect
from typing import Dict


class singleton:
    # Class properties
    _instances: Dict[type, object] = {}
    _testing: bool = False

    # Instance properties
    _cls: type

    def __init__(self, cls):
        signature = inspect.signature(cls.__init__)
        if len(signature.parameters) != 1 and str(signature) != '(self, /, *args, **kwargs)':
            raise KeyError('Constructor arguments are not allowed for singletons. If this '
                           'class is from a third party library, please create a wrapper. '
                           f'Got signature {signature}')
        self._cls = cls

    def __call__(self):
        if singleton._testing or self._cls not in singleton._instances:
            singleton._instances[self._cls] = self._cls()

        return singleton._instances[self._cls]

    @staticmethod
    def testing(enabled: bool = True):
        """
        Set testing to True to disable all singletons
        """
        singleton._testing = enabled
        singleton._instances = {}
