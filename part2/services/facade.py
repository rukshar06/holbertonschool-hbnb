#!/usr/bin/python3
"""Facade for HBNB"""

from app.persistence.repository import InMemoryRepository
from models.user import User


class HBnBFacade:
    """Connect the API to the business logic."""

    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

    def create_user(self, user_data):
        """Create a user."""
        user = User(**user_data)
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        """Get a user by ID."""
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        """Get a user by email."""
        return self.user_repo.get_by_attribute("email", email)

    def get_place(self, place_id):
        """Get a place by ID."""
        return self.place_repo.get(place_id)
