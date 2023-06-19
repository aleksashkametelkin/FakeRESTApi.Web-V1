import json
import random

from faker import Faker

import main as m
from tests.support.assertions import assert_valid_schema
from tests.support.validate import Author

f = Faker()
URL = m.TEST_URL


def test_get_list_of_authors(http_session):
    response = m.get_list_of_authors()
    assert response.status_code == 200

    j = json.loads(response.content)
    assert_valid_schema(j, 'get_list_of_authors.json')


def test_create_author(http_session):
    # Create POST response to create new User
    payload = m.author_payload()
    response = m.create_author(payload)
    assert response.status_code == 200

    Author.id = response.json()["id"]

    j = json.loads(response.content)
    assert_valid_schema(j, 'author.json')


def test_get_author_by_book_id(http_session):
    # Get Author by Author ID
    # API can respond only user ID from 1 to 10
    response = m.get_book_of_author()
    assert response.status_code == 200

    j = json.loads(response.content)
    assert_valid_schema(j, 'get_author_by_book_id.json')


def test_get_author_id(http_session):
    # Get Author by Author ID
    # API can respond only Author ID from 1 to 10
    response = m.get_author_by_id()
    assert response.status_code == 200

    j = json.loads(response.content)
    assert_valid_schema(j, 'author.json')


def test_update_author_by_id(http_session):
    # Update Author's params
    author_id = random.randrange(1, 200)
    book_id = random.randrange(1, 20)
    payload = {
        "id": author_id,
        "idBook": book_id,
        "firstName": f"{f.first_name()}",
        "lastName": f"{f.last_name()}"
    }
    response = m.update_author(payload)
    assert response.status_code == 200
    author_id_new = response.json()["id"]

    assert Author.id != author_id_new
    Author.id = response.json()["id"]

    j = json.loads(response.content)
    assert_valid_schema(j, 'author.json')


def test_delete_author_by_id(http_session):
    # Delete existing activity
    response = m.delete_author()
    assert response.status_code == 200
