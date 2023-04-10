import pytest
from pydantic import BaseModel


class User:
    id: int


class Book:
    id: int
    pageCount: int


class CoverPhoto:
    id: int


class Author:
    id: int


class Activity:
    id: int


@pytest.fixture
def user():
    return User()


@pytest.fixture
def book():
    return BaseModel()
