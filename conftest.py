import pytest
from tests.support.validate import User, Book


@pytest.fixture
def user():
    return User()


@pytest.fixture
def book():
    return Book()
