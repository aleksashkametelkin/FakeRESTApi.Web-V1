import pytest
import requests


@pytest.fixture(autouse=True)
def http_session():
    requests.Session().headers.update({"Content-Type": "application/json"})
    requests.Session().headers.update({"Alex-Auto-Tests": "true"})
