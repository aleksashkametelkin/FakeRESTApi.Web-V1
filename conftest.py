import pytest
from pydantic import BaseModel


@pytest.fixture
def user():
    return BaseModel()


@pytest.fixture
def book():
    return BaseModel()
