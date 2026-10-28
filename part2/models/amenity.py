#!/usr/bin/python3
"""Amenity class """

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Create an amenity."""

    def __init__(self, name):
        super().__init__()

        if type(name) is not str or not name.strip():
            raise ValueError("Name is required")

        if len(name) > 50:
            raise ValueError("Name is too long")

        self.name = name
