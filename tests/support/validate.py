import datetime

from pydantic import BaseModel
from typing import Union, List


class User(BaseModel):
    id: Union[int, str]
    userName: str
    password: str


class Book(BaseModel):
    id: int
    title: str
    description: str
    pageCount: int
    excerpt: str
    publishDate: datetime.datetime


class CoverPhoto(BaseModel):
    id: int
    idBook: int
    url: str


class CoverPhotoArray(BaseModel):
    __root__: List[CoverPhoto]


class Author(BaseModel):
    id: int
    idBook: int
    firstName: str
    lastName: str


class AuthorArray(BaseModel):
    __root__: List[Author]


class Activity(BaseModel):
    id: int
    title: str
    dueDate: datetime.datetime
    completed: bool
