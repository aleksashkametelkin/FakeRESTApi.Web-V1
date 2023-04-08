import datetime
from datetime import datetime
import random

import requests
from faker import Faker
from utils.models import BaseClass

f = Faker()
TEST_URL = "https://fakerestapi.azurewebsites.net"


# Activities
def get_list_of_activities():
    return requests.get(TEST_URL + f"/api/v1/Activities")


def create_activity(activity_id):
    return requests.post(TEST_URL + f"/api/v1/Activities/{activity_id}", json=activity_id)


def get_activity():
    return requests.get(TEST_URL + f"/api/v1/Activities/{BaseClass.id}")


def update_activity(activity_id):
    return requests.put(TEST_URL + f"/api/v1/Activities/{BaseClass.id}", json=activity_id)


def delete_activity(activity_id):
    return requests.delete(TEST_URL + f"/api/v1/Activities/{activity_id}")


def activity_payload():
    activity_id = random.randrange(1, 200)
    return {
        "id": activity_id,
        "title": f"{f.job()}",
        "dueDate": f"2023-04-07T16:22:19.253Z",
        "completed": True,
    }


# Authors
def get_list_of_authors():
    return requests.get(TEST_URL + f"/api/v1/Authors")


def create_author(author):
    return requests.post(TEST_URL + f"/api/v1/Authors", json=author)


def get_book_of_author():
    return requests.get(TEST_URL + f"/api/v1/Authors/authors/books/{BaseClass.id}")


def get_author_by_id():
    return requests.get(TEST_URL + f"/api/v1/Authors/{BaseClass.id}")


def update_author(author):
    return requests.put(TEST_URL + f"/api/v1/Authors/{BaseClass.id}", json=author)


def delete_author():
    return requests.put(TEST_URL + f"/api/v1/Authors/{BaseClass.id}")


def author_payload():
    author_id = random.randrange(1, 200)
    book_id = random.randrange(1, 200)
    return {
        "id": author_id,
        "idBook": book_id,
        "firstName": f"{f.first_name()}",
        "lastName": f"{f.last_name()}"
    }


# Books
def get_list_of_books():
    return requests.get(TEST_URL + f"/api/v1/Books")


def create_book(activity):
    return requests.post(TEST_URL + f"/api/v1/Books", json=activity)


def get_book_by_id():
    return requests.get(TEST_URL + f"/api/v1/Books/{BaseClass.id}")


def update_book(activity):
    return requests.put(TEST_URL + f"/api/v1/Books/{BaseClass.id}", json=activity)


def delete_book():
    return requests.delete(TEST_URL + f"/api/v1/Books/{BaseClass.id}")


def book_payload():
    # date_now = datetime.date.today()
    # time_now = datetime.time.
    book_id = random.randrange(1, 10)
    page_count = random.randrange(100, 2000)

    return {
        "id": book_id,
        "title": f"{f.name()}",
        "description": f"{f.job()}",
        "pageCount": page_count,
        "excerpt": "string",
        "publishDate": "2023-04-05T22:44:04.097Z"
    }


# CoverPhotos
def get_list_of_cover_photos():
    return requests.get(TEST_URL + f"/api/v1/Authors")


def create_cover_photo(author):
    return requests.post(TEST_URL + f"/api/v1/Authors", params=author)


def get_book_by_cover_photo():
    return requests.get(TEST_URL + f"/api/v1/Authors{BaseClass.id}")


def get_cover_photo_by_id():
    return requests.get(TEST_URL + f"/api/v1/Authors/authors/books/{BaseClass}")


def update_cover_photo(author):
    return requests.put(TEST_URL + f"/api/v1/Authors", params=author)


def delete_cover_photo(author):
    return requests.put(TEST_URL + f"/api/v1/Authors", params=author)


def cover_photo_payload():
    return {
        "id": 0,
        "idBook": 0,
        "url": "string"
    }


# Users
def get_list_of_users():
    return requests.get(TEST_URL + f"/api/v1/Users")


def create_user(user_id):
    return requests.post(TEST_URL + f"/api/v1/Users", json=user_id)


def get_user_by_id():
    return requests.get(TEST_URL + f"/api/v1/Users/{BaseClass.id}")


def update_user(user_id):
    return requests.put(TEST_URL + f"/api/v1/Users/{BaseClass.id}", json=user_id)


def delete_user():
    return requests.delete(TEST_URL + f"/api/v1/Users/{BaseClass.id}")


def user_payload():
    # API can respond only Integer user ID: from 1 to 10
    user_id = random.randrange(1, 10)
    return {
        "id": user_id,
        "userName": f"{f.name()}",
        "password": f"{f.password()}"
    }
