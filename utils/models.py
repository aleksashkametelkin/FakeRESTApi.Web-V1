from pydantic import BaseModel
from typing import Optional


class BaseClass(BaseModel):
    # User
    id: Optional[int]
    name: Optional[str]
    password: Optional[str]
    # Activity
    title: Optional[str]
    dueDate: Optional[str]
    completed: Optional[bool]
    # Author
    idBook: Optional[int]
    firstName: Optional[str]
    lastName: Optional[str]
    # CoverPhotos
    url: Optional[str]


class Book(BaseModel):
    # Book
    id: Optional[int]
    title: Optional[str]
    description: Optional[str]
    pageCount: Optional[int]
    excerpt: Optional[str]
    publishDate: Optional[str]
