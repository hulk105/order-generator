from builtins import Exception, BaseException


class HexStringError(Exception):
    def __init__(self, arg="Wrong hex value{}"):
        self.message = f"Wrong hex value '{arg}'"
        super().__init__(self.message)
