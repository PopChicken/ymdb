class AuthException(Exception):
    def __init__(self, msg: str) -> None:
        super().__init__()
        self.msg: str = msg


class ServiceException(Exception):
    def __init__(self, msg: str) -> None:
        super().__init__()
        self.msg: str = msg