from pydantic import BaseModel
from typing import Optional
import random

import requests
from faker import Faker


class User(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    password: Optional[str]


f = Faker()
TEST_URL = "https://fakerestapi.azurewebsites.net"


# Activities
def get_list_of_activities():
    return requests.get(TEST_URL + f"/api/v1/Activities")


def create_activity(activity):
    return requests.post(TEST_URL + f"/api/v1/Activities", params=activity)


def get_activity(activity):
    return requests.get(TEST_URL + f"/api/v1/Activities", params=activity)


def update_activity(activity):
    return requests.put(TEST_URL + f"/api/v1/Activities", params=activity)


def delete_activity(activity):
    return requests.put(TEST_URL + f"/api/v1/Activities", params=activity)


def author_payload():
    return {
        "id": 64577354,
        "title": "string",
        "dueDate": "2023-04-05T17:36:23.298Z",
        "completed": False
    }


# Authors
def get_list_of_authors():
    return requests.get(TEST_URL + f"/api/v1/Authors")


def create_author(author):
    return requests.post(TEST_URL + f"/api/v1/Authors", params=author)


def get_book_of_author(author):
    return requests.get(TEST_URL + f"/api/v1/Authors", params=author)


def get_author_by_id(book):
    return requests.get(TEST_URL + f"/api/v1/Authors/authors/books/", params=book)


def update_author(author):
    return requests.put(TEST_URL + f"/api/v1/Authors", params=author)


def delete_author(author):
    return requests.put(TEST_URL + f"/api/v1/Authors", params=author)


def author_payload():
    return {
        "id": 0,
        "idBook": 0,
        "firstName": "string",
        "lastName": "string"
    }


# Books
def get_list_of_books():
    return requests.get(TEST_URL + f"/api/v1/Activities")


def create_book(activity):
    return requests.post(TEST_URL + f"/api/v1/Activities", params=activity)


def get_book_by_id(activity):
    return requests.get(TEST_URL + f"/api/v1/Activities", params=activity)


def update_book(activity):
    return requests.put(TEST_URL + f"/api/v1/Activities", params=activity)


def delete_book(activity):
    return requests.put(TEST_URL + f"/api/v1/Activities", params=activity)


def book_payload():
    return {
        "id": 0,
        "title": "string",
        "description": "string",
        "pageCount": 0,
        "excerpt": "string",
        "publishDate": "2023-04-05T22:44:04.097Z"
    }


# CoverPhotos
def get_list_of_cover_photos():
    return requests.get(TEST_URL + f"/api/v1/Authors")


def create_cover_photo(author):
    return requests.post(TEST_URL + f"/api/v1/Authors", params=author)


def get_book_by_cover_photo(author):
    return requests.get(TEST_URL + f"/api/v1/Authors", params=author)


def get_cover_photo_by_id(book):
    return requests.get(TEST_URL + f"/api/v1/Authors/authors/books/", params=book)


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


def get_user_by_id(user_id):
    return requests.get(TEST_URL + f"/api/v1/Users/{user_id}")


def update_user(user_id):
    return requests.put(TEST_URL + f"/api/v1/Users/{User.id}", json=user_id)


def delete_user(user):
    return requests.put(TEST_URL + f"/api/v1/Users/{user}")


def user_payload():
    # API can respond only Integer user ID: from 1 to 10
    user_id = random.randrange(1, 10)
    return {
        "id": user_id,
        "userName": f"{f.name()}",
        "password": f"{f.password()}"
    }
