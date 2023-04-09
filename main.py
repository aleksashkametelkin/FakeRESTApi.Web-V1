import random

import requests
from faker import Faker
from utils.models import BaseClass, Book

f = Faker()
TEST_URL = "https://fakerestapi.azurewebsites.net"


# Activities
def get_list_of_activities():
    return requests.get(TEST_URL + f"/api/v1/Activities")


def create_activity(activity):
    return requests.post(TEST_URL + f"/api/v1/Activities", json=activity)


def get_activity():
    return requests.get(TEST_URL + f"/api/v1/Activities/{BaseClass.id}")


def update_activity(activity):
    return requests.put(TEST_URL + f"/api/v1/Activities/{BaseClass.id}", json=activity)


def delete_activity():
    return requests.delete(TEST_URL + f"/api/v1/Activities/{BaseClass.id}")


def activity_payload():
    activity_id = random.randrange(1, 10)
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
    return requests.delete(TEST_URL + f"/api/v1/Authors/{BaseClass.id}")


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
    return requests.get(TEST_URL + f"/api/v1/Books/{Book.id}")


def update_book(activity):
    return requests.put(TEST_URL + f"/api/v1/Books/{Book.id}", json=activity)


def delete_book():
    return requests.delete(TEST_URL + f"/api/v1/Books/{Book.id}")


def book_payload():
    book_id = random.randrange(1, 10)
    page_count = random.randrange(100, 200)

    return {
        "id": book_id,
        "title": f"{f.name()}",
        "description": f"{f.job()}",
        "pageCount": page_count,
        "excerpt": "strttrtdgd",
        "publishDate": "2023-04-05T22:44:04.097Z"
    }


# CoverPhotos
def get_list_of_cover_photos():
    return requests.get(TEST_URL + f"/api/v1/CoverPhotos")


def create_cover_photo(cover_photo):
    return requests.post(TEST_URL + f"/api/v1/CoverPhotos", json=cover_photo)


def get_cover_photo_by_book_id():
    return requests.get(TEST_URL + f"/api/v1/CoverPhotos/books/covers/{Book.id}")


def get_cover_photo_by_id():
    return requests.get(TEST_URL + f"/api/v1/CoverPhotos/{BaseClass.id}")


def update_cover_photo(cover_photo):
    return requests.put(TEST_URL + f"/api/v1/CoverPhotos/{BaseClass.id}", json=cover_photo)


def delete_cover_photo():
    return requests.delete(TEST_URL + f"/api/v1/CoverPhotos/{BaseClass.id}")


def cover_photo_payload():
    cover_photo_id = random.randrange(1, 10)
    book_id = random.randrange(1, 200)
    return {
        "id": cover_photo_id,
        "idBook": book_id,
        "url": f"{f.url()}"
    }


# Users
def get_list_of_users():
    return requests.get(TEST_URL + f"/api/v1/Users")


def create_user(user):
    return requests.post(TEST_URL + f"/api/v1/Users", json=user)


def get_user_by_id():
    return requests.get(TEST_URL + f"/api/v1/Users/{BaseClass.id}")


def update_user(user):
    return requests.put(TEST_URL + f"/api/v1/Users/{BaseClass.id}", json=user)


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
