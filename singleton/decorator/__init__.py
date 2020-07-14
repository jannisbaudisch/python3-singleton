class singleton:
    _cls: type
    _instance: object
    _testing: bool = False

    def __init__(self, cls):
        self._cls = cls
        self._instance = None

    def __call__(self, *args, **kwargs):
        if self._instance is None or singleton._testing:
            self._instance = self._cls()

        return self._instance

    @classmethod
    def testing(cls):
        """
        Set testing to True to disable all singletons
        """
        cls._testing = True
