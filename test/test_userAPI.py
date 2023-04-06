import main as m
# from main import User

URL = m.TEST_URL


def test_get_list_of_users():
    response = m.get_list_of_users()
    assert response.status_code == 200


def test_create_user():
    # Create POST response to create new User
    payload = m.user_payload()
    response = m.create_user(payload)
    assert response.status_code == 200
    id = response.json()["id"]
    # print(id)

    return id


ret = test_create_user()


def test_get_user_by_id(ret):
    # Get User by User ID
    payload = m.get_user_by_id()
    response = m.get_user_by_id()
    assert response.status_code == 200

