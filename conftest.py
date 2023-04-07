import pytest
from main import User


@pytest.fixture
def user():
    return User()
