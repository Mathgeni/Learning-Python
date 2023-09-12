from requests import Session


class SessionManger:
    """
    Context manager for Session object from request package
    """
    def __init__(self):
        self.session = Session()

    def __enter__(self):
        return self.session

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
