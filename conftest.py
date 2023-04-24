import pytest
import requests
from tests.support.validate import User, Book


@pytest.fixture
def user(scope="session"):
    return User()


@pytest.fixture
def book(scope="session"):
    return Book()


@pytest.fixture
def http_session(scope="session"):
    with requests.Session() as s:
        s.headers.update({"Content-Type": "application/json"})
        s.headers.update({"X-Test": "true"})
        yield s
