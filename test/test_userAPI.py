import main as m

URL = m.TEST_URL


def test_get_list_of_users():
    response = m.get_list_of_users()
    assert response.status_code == 200


def test_create_user():
    # Create POST response to create new User
    payload = m.user_payload()
    response = m.create_user(payload)
    assert response.status_code == 200
    data = response.json()["id"]
    print(data)

    return data


def test_get_user_by_id():
    # Get User by User ID
    # API can respond only user ID from 1 to 10
    u = test_create_user()
    response = m.get_user_by_id(u)
    assert response.status_code == 200


def test_update_user_by_id():
    pass