#!/usr/bin/python3
"""Define a function for class Review"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Review a place."""

    def __init__(self, text, rating, place, user):
        super().__init__()

        if type(text) is not str or not text:
            raise ValueError("Text is required")

        if type(rating) is not int:
            raise TypeError("Rating must be an integer")

        if rating < 1 or rating > 5:
            raise ValueError("Rating must be between 1 and 5")

        if place is None or user is None:
            raise ValueError("Place and user are required")

        self.text = text
        self.rating = rating
        self.place = place
        self.user = user
