import pytest


class User:

    def __init__(self) -> None:
        self.name = None
        self.second_name = None

    def create(self):
        self.name = 'Lesia'
        self.second_name = 'Stefaniv'

    def remove(self):
        self.name = ''
        self.second_name = ''


@pytest.fixture
def user():
    user = User()
    user.create()

    yield user  #everything before this line is executed before the test, everything after - after the test
    
    user.remove()
    
