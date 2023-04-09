import main as m
from utils.models import Book

from tests.support.assertions import assert_valid_schema

URL = m.TEST_URL


def test_get_list_of_books():
    response = m.get_list_of_books()
    assert response.status_code == 200


def test_create_book(user: Book):
    # Create POST response to create new User
    payload = m.book_payload()
    response = m.create_book(payload)
    assert response.status_code == 200

    Book.id = response.json()["id"]


def test_get_book_by_id():
    # Get User by User ID
    # API can respond only user ID from 1 to 10
    response = m.get_book_by_id()
    assert response.status_code == 200


def test_update_book_by_id(user: Book):
    # Update User's params
    payload = m.book_payload()
    response = m.update_book(payload)
    assert response.status_code == 200
    book_id_new = response.json()["id"]

    assert Book.id != book_id_new
    Book.id = response.json()["id"]


def test_delete_book():
    response = m.get_book_by_id()
    assert response.status_code == 200
