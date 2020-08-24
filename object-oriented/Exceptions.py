from sys import exit
from builtins import Exception, BaseException


class HexStringError(Exception):
    def __init__(self, arg):
        self.message = f"Value '{arg}' is not hexadecimal"
        super().__init__(self.message)


class InvalidConfigurationError(Exception):
    def __init__(self, exception: Exception):
        self.message = f"Invalid configuration from: {exception}"
        super().__init__(self.message)
        exit(1)
