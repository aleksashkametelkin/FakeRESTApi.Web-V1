import json
import random
import main as m
from conftest import Book

from tests.support.assertions import assert_valid_schema

URL = m.TEST_URL


def test_get_list_of_books():
    response = m.get_list_of_books()
    assert response.status_code == 200

    j = json.loads(response.content)
    assert_valid_schema(j, 'get_list_of_books.json')


def test_create_book(book: Book):
    # Create POST response to create new Book
    payload = m.book_payload()
    response = m.create_book(payload)
    assert response.status_code == 200

    Book.id = response.json()["id"]
    Book.pageCount = response.json()["pageCount"]

    j = json.loads(response.content)
    assert_valid_schema(j, 'book.json')


def test_get_book_by_id():
    # Get User by User ID
    # API can respond only user ID from 1 to 10
    response = m.get_book_by_id()
    assert response.status_code == 200

    j = json.loads(response.content)
    assert_valid_schema(j, 'book.json')


def test_update_book_by_id(book: Book):
    # Update Book params
    book_id = random.randrange(100, 1000)
    page_count = random.randrange(1000, 10000)
    payload = {
        "id": book_id,
        "title": "test title",
        "description": "test description",
        "pageCount": page_count,
        "excerpt": "Str",
        "publishDate": "2023-04-09T09:48:47.895Z"
    }
    response = m.update_book(payload)
    assert response.status_code == 200
    book_id_new = response.json()["id"]
    page_count_new = response.json()["pageCount"]

    assert Book.id != book_id_new
    assert Book.pageCount != page_count_new
    Book.id = response.json()["id"]

    j = json.loads(response.content)
    assert_valid_schema(j, 'book.json')


def test_delete_book():
    response = m.delete_book()
    assert response.status_code == 200
