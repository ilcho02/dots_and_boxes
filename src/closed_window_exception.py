class ClosedWindowException(Exception):
    def __init__(self, message:str='The window is closed'):
        super().__init__(message)