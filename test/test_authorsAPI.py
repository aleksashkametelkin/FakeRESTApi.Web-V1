import main as m
from main import BaseClass

URL = m.TEST_URL


def test_get_list_of_authors():
    response = m.get_list_of_authors()
    assert response.status_code == 200


def test_create_author(user: BaseClass):
    # Create POST response to create new User
    payload = m.author_payload()
    response = m.create_author(payload)
    assert response.status_code == 200

    BaseClass.id = response.json()["id"]


# def test_get_book_by_author_id():
#     # Get Author by Author ID
#     # API can respond only user ID from 1 to 10
#     response = m.get_book_of_author()
#     assert response.status_code == 200
#     pass


def test_get_author_id():
    # Get Author by Author ID
    # API can respond only user ID from 1 to 10
    # response = m.get_author_by_id(Book.id)
    # assert response.status_code == 200
    pass


def test_update_author_by_id(user: BaseClass):
    # Update User's params
    payload = m.author_payload()
    print(payload)
    response = m.update_author(payload)
    print(response)
    assert response.status_code == 200
    author_id_new = response.json()["id"]
    print(author_id_new)

    assert BaseClass.id != author_id_new
    BaseClass.id = response.json()["id"]


def test_delete_author_by_id():
    # Delete existing activity
    payload = m.author_payload()
    response = m.update_author(payload)
    assert response.status_code == 200
    author_id_new = response.json()["id"]

    assert BaseClass.id != author_id_new
    BaseClass.id = response.json()["id"]
