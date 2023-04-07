import main as m
from main import BaseClass

URL = m.TEST_URL


def test_get_list_of_activities():
    response = m.get_list_of_users()
    assert response.status_code == 200


def test_create_activity(user: BaseClass):
    # Create POST response to create new Activity
    payload = m.user_payload()
    response = m.create_user(payload)
    assert response.status_code == 200

    BaseClass.id = response.json()["id"]


def test_get_activity_id():
    # Get Activity by ID
    # API can respond only Activity ID from 1 to 10
    response = m.get_user_by_id(BaseClass.id)
    assert response.status_code == 200


def test_update_activity_by_id(user: BaseClass):
    # Update Activity's params
    payload = m.activity_payload()
    response = m.update_activity(payload)
    assert response.status_code == 200
    activiti_id_new = response.json()["id"]

    assert BaseClass.id != activiti_id_new
    BaseClass.id = response.json()["id"]


def test_delete_activity_by_id():
    # Delete existing activity
    payload = m.activity_payload()
    response = m.update_activity(payload)
    assert response.status_code == 200
    activity_id_new = response.json()["id"]

    assert BaseClass.id != activity_id_new
    BaseClass.id = response.json()["id"]
