import json
import random
import main as m
from conftest import CoverPhoto

from faker import Faker

from tests.support.assertions import assert_valid_schema

f = Faker()
URL = m.TEST_URL


def test_get_list_of_cover_photos():
    response = m.get_list_of_cover_photos()
    assert response.status_code == 200

    j = json.loads(response.content)
    assert_valid_schema(j, 'get_list_of_cover_photos.json')


def test_create_cover_photo(user: CoverPhoto):
    # Create POST response to create new User
    payload = m.cover_photo_payload()
    response = m.create_cover_photo(payload)
    assert response.status_code == 200

    CoverPhoto.id = response.json()["id"]

    j = json.loads(response.content)
    assert_valid_schema(j, 'cover_photo.json')


def test_get_cover_photo_by_book_id():
    # Get Author by Author ID
    # API can respond only user ID from 1 to 10
    response = m.get_cover_photo_by_book_id()
    assert response.status_code == 200

    j = json.loads(response.content)
    assert_valid_schema(j, 'get_cover_photo_by_book_id.json')


def test_get_cover_photo_by_id():
    # Get Author by Author ID
    # API can respond only user ID from 1 to 10
    response = m.get_cover_photo_by_id()
    assert response.status_code == 200

    j = json.loads(response.content)
    assert_valid_schema(j, 'cover_photo.json')


def test_update_cover_photo_by_id(user: CoverPhoto):
    # Update Cover photo params
    cover_photo_id = random.randrange(11, 1000)
    book_id = random.randrange(1, 200)
    payload = {
        "id": cover_photo_id,
        "idBook": book_id,
        "url": f"{f.url()}"
    }
    response = m.update_cover_photo(payload)
    assert response.status_code == 200
    cover_photo_id_new = response.json()["id"]

    assert CoverPhoto.id != cover_photo_id_new
    CoverPhoto.id = response.json()["id"]

    j = json.loads(response.content)
    assert_valid_schema(j, 'cover_photo.json')


def test_delete_cover_photo_by_id():
    # Delete existing cover photo
    response = m.delete_cover_photo()
    assert response.status_code == 200
