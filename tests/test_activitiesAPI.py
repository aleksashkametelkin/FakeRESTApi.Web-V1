import json
import random
import main as m
from tests.support.validate import Activity

from tests.support.assertions import assert_valid_schema

URL = m.TEST_URL


def test_get_list_of_activities():
    response = m.get_list_of_activities()
    assert response.status_code == 200

    j = json.loads(response.content)
    assert_valid_schema(j, 'get_list_of_activities.json')


def test_create_activity():
    # Create POST response to create new Activity
    payload = m.activity_payload()
    response = m.create_activity(payload)
    assert response.status_code == 200

    Activity.id = response.json()["id"]

    j = json.loads(response.content)
    assert_valid_schema(j, 'activity.json')


def test_get_activity_id():
    # Get Activity by ID
    # API can respond only Activity ID from 1 to 10
    response = m.get_activity()
    assert response.status_code == 200

    j = json.loads(response.content)
    assert_valid_schema(j, 'activity.json')


def test_update_activity_by_id():
    # Update Activity's params
    activity_id = random.randrange(100, 1000)
    payload = {
        "activity_id": activity_id,
        "title": "test title",
        "dueDate": "2023-04-09T09:39:20.165Z",
        "completed": True
    }
    response = m.update_activity(payload)
    assert response.status_code == 200
    activiti_id_new = response.json()["id"]

    assert Activity.id != activiti_id_new
    Activity.id = response.json()["id"]

    j = json.loads(response.content)
    assert_valid_schema(j, 'activity.json')


def test_delete_activity_by_id():
    # Delete existing activity
    response = m.delete_activity()
    assert response.status_code == 200
