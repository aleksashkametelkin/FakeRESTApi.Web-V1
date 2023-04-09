import main as m
import random
import json
from utils.models import BaseClass

from faker import Faker
from tests.support.assertions import assert_valid_schema

f = Faker()
URL = m.TEST_URL


def test_get_list_of_users():
    response = m.get_list_of_users()
    assert response.status_code == 200

    j = json.loads(response.content)
    assert_valid_schema(j, 'get_list_of_users.json')


def test_create_user(user: BaseClass):
    # Create POST response to create new User
    payload = m.user_payload()
    response = m.create_user(payload)
    assert response.status_code == 200

    BaseClass.id = response.json()["id"]

    j = json.loads(response.content)
    assert_valid_schema(j, 'user.json')


def test_get_user_by_id():
    # Get User by User ID
    # API can respond only user ID from 1 to 10
    response = m.get_user_by_id()
    assert response.status_code == 200

    j = json.loads(response.content)
    assert_valid_schema(j, 'user.json')


def test_update_user_by_id(user: BaseClass):
    # Update User's params
    user_id = random.randrange(100, 1000)
    payload = {
        "id": user_id,
        "userName": f"{f.name()}",
        "password": f"{f.password()}"
    }
    response = m.update_user(payload)
    assert response.status_code == 200
    user_id_new = response.json()["id"]

    assert BaseClass.id != user_id_new
    BaseClass.id = response.json()["id"]

    j = json.loads(response.content)
    assert_valid_schema(j, 'user.json')


def test_delete_user():
    response = m.delete_user()
    assert response.status_code == 200
