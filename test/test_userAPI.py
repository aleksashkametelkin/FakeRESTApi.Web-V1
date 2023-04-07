import main as m
from main import BaseClass

URL = m.TEST_URL


def test_get_list_of_users():
    response = m.get_list_of_users()
    assert response.status_code == 200


def test_create_user(user: BaseClass):
    # Create POST response to create new User
    payload = m.user_payload()
    response = m.create_user(payload)
    assert response.status_code == 200

    BaseClass.id = response.json()["id"]


def test_get_user_by_id():
    # Get User by User ID
    # API can respond only user ID from 1 to 10
    response = m.get_user_by_id(BaseClass.id)
    assert response.status_code == 200


def test_update_user_by_id(user: BaseClass):
    # Update User's params
    payload = m.user_payload()
    response = m.update_user(payload)
    assert response.status_code == 200
    user_id_new = response.json()["id"]

    assert BaseClass.id != user_id_new
    BaseClass.id = response.json()["id"]


def test_delete_user():
    response = m.get_user_by_id(BaseClass.id)
    assert response.status_code == 200
