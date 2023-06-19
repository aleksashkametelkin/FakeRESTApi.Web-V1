import pytest
import requests


@pytest.fixture
def http_session(scope="session"):
    with requests.Session() as s:
        s.headers.update({"Content-Type": "application/json"})
        s.headers.update({"X-Test": "true"})
        yield s
        