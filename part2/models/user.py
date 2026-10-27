#!/usr/bin/python3
"""Define a function for User class"""

import re
from models.base_model import BaseModel


class User(BaseModel):
    """Create a user."""

    def __init__(self, first_name, last_name, email, is_admin=False):
        super().__init__()

        if type(first_name) is not str or not first_name.strip():
            raise ValueError("First name is required")
        if len(first_name) > 50:
            raise ValueError("First name is too long")

        if type(last_name) is not str or not last_name.strip():
            raise ValueError("Last name is required")
        if len(last_name) > 50:
            raise ValueError("Last name is too long")

        if type(email) is not str:
            raise ValueError("Email must be a string")

        if not re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", email):
            raise ValueError("Invalid email")

        if type(is_admin) is not bool:
            raise ValueError("is_admin must be True or False")

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin

        self.places = []
        self.reviews = []
