from pydantic import BaseModel
from typing import List
from datetime import datetime


class BookDataModel(BaseModel):
    """

    """
    book_summaries: str
    last_read: datetime


class BookInfos(BaseModel):
    """
    to collect all infos about the book using  Google API
    """
    book_category: list
    book_pages: int
    book_image: str
