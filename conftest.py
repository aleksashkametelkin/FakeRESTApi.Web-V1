import pytest
from utils.models import BaseClass


@pytest.fixture
def user():
    return BaseClass()
