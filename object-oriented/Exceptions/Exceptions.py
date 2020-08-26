from builtins import Exception


class HexStringError(Exception):
    def __init__(self, message):
        self.message = f"Value '{message}' is not hexadecimal"
        super().__init__(self.message)


class InvalidConfigurationError(Exception):
    def __init__(self, message):
        self.message = f"Invalid configuration from: {message}"
        super().__init__(self.message)
