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
    # Book
    description: Optional[str]
    pageCount: Optional[int]
    excerpt: Optional[str]
    publishDate: Optional[str]
    # CoverPhotos
    url: Optional[str]