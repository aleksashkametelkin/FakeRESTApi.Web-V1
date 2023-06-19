import pytest
import requests


@pytest.fixture(scope="session")
def http_session():
    requests.Session().headers.update({"Content-Type": "application/json"})
    requests.Session().headers.update({"Alex-Auto-Tests": "true"})
