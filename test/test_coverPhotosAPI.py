import main as m
from utils.models import BaseClass

URL = m.TEST_URL


def test_get_list_of_cover_photos():
    response = m.get_list_of_cover_photos()
    assert response.status_code == 200


def test_create_cover_photo(user: BaseClass):
    # Create POST response to create new User
    payload = m.cover_photo_payload()
    response = m.create_cover_photo(payload)
    assert response.status_code == 200

    BaseClass.id = response.json()["id"]


def test_get_cover_photo_by_book_id():
    # Get Author by Author ID
    # API can respond only user ID from 1 to 10
    response = m.get_cover_photo_by_book_id()
    assert response.status_code == 200


def test_get_cover_photo_id():
    # Get Author by Author ID
    # API can respond only user ID from 1 to 10
    response = m.get_cover_photo_by_id()
    assert response.status_code == 200


def test_update_cover_photo_by_id(user: BaseClass):
    # Update User's params
    payload = m.cover_photo_payload()
    response = m.update_cover_photo(payload)
    assert response.status_code == 200
    cover_photo_id_new = response.json()["id"]

    assert BaseClass.id != cover_photo_id_new
    BaseClass.id = response.json()["id"]


def test_delete_cover_photo_by_id():
    # Delete existing activity
    payload = m.cover_photo_payload()
    response = m.delete_cover_photo(payload)
    assert response.status_code == 200
    cover_photo_id_new = response.json()["id"]

    assert BaseClass.id != cover_photo_id_new
    BaseClass.id = response.json()["id"]
