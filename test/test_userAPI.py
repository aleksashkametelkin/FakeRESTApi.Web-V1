import main as m
from main import User

URL = m.TEST_URL


def test_get_list_of_users():
    response = m.get_list_of_users()
    assert response.status_code == 200


def test_create_user(user: User):
    # Create POST response to create new User
    payload = m.user_payload()
    response = m.create_user(payload)
    assert response.status_code == 200

    User.id = response.json()["id"]


def test_get_user_by_id(user: User):
    # Get User by User ID
    # API can respond only user ID from 1 to 10
    response = m.get_user_by_id(User.id)
    assert response.status_code == 200


def test_update_user_by_id():
    pass
