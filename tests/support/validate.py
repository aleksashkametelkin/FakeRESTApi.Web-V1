from pydantic import BaseModel, validator


class User:
    id: int


class Book:
    id: int
    pageCount: int


class CoverPhoto:
    id: int


class Author:
    id: int


class Activity:
    id: int


