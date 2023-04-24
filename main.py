import random

import requests
from faker import Faker
from tests.support.validate import User, Book, CoverPhoto, Author, Activity

f = Faker()
TEST_URL = "https://fakerestapi.azurewebsites.net"


# Activities
def get_list_of_activities():
    return requests.get(TEST_URL + f"/api/v1/Activities")


def create_activity(payload):
    return requests.post(TEST_URL + f"/api/v1/Activities", json=payload)


def get_activity():
    return requests.get(TEST_URL + f"/api/v1/Activities/{Activity.id}")


def update_activity(payload):
    return requests.put(TEST_URL + f"/api/v1/Activities/{Activity.id}", json=payload)


def delete_activity():
    return requests.delete(TEST_URL + f"/api/v1/Activities/{Activity.id}")


def activity_payload():
    return {
        "id": f"{random.randrange(1, 10)}",
        "title": f"{f.job()}",
        "dueDate": f"2023-04-07T16:22:19.253Z",
        "completed": True,
    }


# Authors
def get_list_of_authors():
    return requests.get(TEST_URL + f"/api/v1/Authors")


def create_author(payload):
    return requests.post(TEST_URL + f"/api/v1/Authors", json=payload)


def get_book_of_author():
    return requests.get(TEST_URL + f"/api/v1/Authors/authors/books/{Author.id}")


def get_author_by_id():
    return requests.get(TEST_URL + f"/api/v1/Authors/{Author.id}")


def update_author(payload):
    return requests.put(TEST_URL + f"/api/v1/Authors/{Author.id}", json=payload)


def delete_author():
    return requests.delete(TEST_URL + f"/api/v1/Authors/{Author.id}")


def author_payload():
    return {
        "id": f"{random.randrange(1, 200)}",
        "idBook": f"{random.randrange(1, 200)}",
        "firstName": f"{f.first_name()}",
        "lastName": f"{f.last_name()}"
    }


# Books
def get_list_of_books():
    return requests.get(TEST_URL + f"/api/v1/Books")


def create_book(payload):
    return requests.post(TEST_URL + f"/api/v1/Books", json=payload)


def get_book_by_id():
    return requests.get(TEST_URL + f"/api/v1/Books/{Book.id}")


def update_book(payload):
    return requests.put(TEST_URL + f"/api/v1/Books/{Book.id}", json=payload)


def delete_book():
    return requests.delete(TEST_URL + f"/api/v1/Books/{Book.id}")


def book_payload():
    return {
        "id": f"{random.randrange(1, 10)}",
        "title": f"{f.name()}",
        "description": f"{f.job()}",
        "pageCount": f"{random.randrange(100, 200)}",
        "excerpt": "strttrtdgd",
        "publishDate": "2023-04-05T22:44:04.097Z"
    }


# CoverPhotos
def get_list_of_cover_photos():
    return requests.get(TEST_URL + f"/api/v1/CoverPhotos")


def create_cover_photo(payload):
    return requests.post(TEST_URL + f"/api/v1/CoverPhotos", json=payload)


def get_cover_photo_by_book_id():
    return requests.get(TEST_URL + f"/api/v1/CoverPhotos/books/covers/{Book.id}")


def get_cover_photo_by_id():
    return requests.get(TEST_URL + f"/api/v1/CoverPhotos/{CoverPhoto.id}")


def update_cover_photo(payload):
    return requests.put(TEST_URL + f"/api/v1/CoverPhotos/{CoverPhoto.id}", json=payload)


def delete_cover_photo():
    return requests.delete(TEST_URL + f"/api/v1/CoverPhotos/{CoverPhoto.id}")


def cover_photo_payload():
    return {
        "id": f"{random.randrange(1, 10)}",
        "idBook": f"{random.randrange(1, 20)}",
        "url": f"{f.url()}"
    }


# Users
def get_list_of_users():
    return requests.get(TEST_URL + f"/api/v1/Users")


def create_user(payload):
    return requests.post(TEST_URL + f"/api/v1/Users", json=payload)


def get_user_by_id():
    return requests.get(TEST_URL + f"/api/v1/Users/{User.id}")


def update_user(payload):
    return requests.put(TEST_URL + f"/api/v1/Users/{User.id}", json=payload)


def delete_user():
    return requests.delete(TEST_URL + f"/api/v1/Users/{User.id}")


def user_payload():
    # API can respond only Integer user ID: from 1 to 10
    return {
        "id": f"{random.randrange(1, 10)}",
        "userName": f"{f.name()}",
        "password": f"{f.password()}"
    }
