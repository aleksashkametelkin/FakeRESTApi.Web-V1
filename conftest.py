import pytest
from main import BaseClass


@pytest.fixture
def user():
    return BaseClass()
