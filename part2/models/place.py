#!/usr/bin/python3
"""Place class for HBnB."""

from models.base_model import BaseModel
from models.user import User


class Place(BaseModel):
    """Create a place."""

    def __init__(self, title, description, price, latitude, longitude, owner):
        super().__init__()

        if type(title) is not str or not title.strip():
            raise ValueError("Title is required")
        if len(title) > 100:
            raise ValueError("Title is too long")

        if type(description) is not str:
            raise TypeError("Description must be a string")

        if type(price) is not int and type(price) is not float:
            raise TypeError("Price must be a number")
        if price < 0:
            raise ValueError("Price cannot be negative")

        if type(latitude) is not int and type(latitude) is not float:
            raise TypeError("Latitude must be a number")

        if latitude < -90 or latitude > 90:
            raise ValueError("Invalid latitude")

        if type(longitude) is not int and type(longitude) is not float:
            raise TypeError("Longitude must be a number")

        if longitude < -180 or longitude > 180:
            raise ValueError("Invalid longitude")

        if type(owner) is not User:
            raise TypeError("Owner must be a User")

        self.title = title
        self.description = description
        self.price = float(price)
        self.latitude = float(latitude)
        self.longitude = float(longitude)
        self.owner = owner

        self.reviews = []
        self.amenities = []

    def add_review(self, review):
        """Add a review to the place."""
        self.reviews.append(review)

    def add_amenity(self, amenity):
        """Add an amenity to the place."""
        self.amenities.append(amenity)

    def update(self, place_data):
        """Update place information."""

        if 'title' in place_data:
            title = place_data['title']

            if type(title) is not str or not title.strip():
                raise ValueError("Title is required")

            if len(title) > 100:
                raise ValueError("Title is too long")

            self.title = title

        if 'description' in place_data:
            description = place_data['description']

            if type(description) is not str:
                raise TypeError("Description must be a string")

            self.description = description

        if 'price' in place_data:
            price = place_data['price']

            if type(price) is not int and type(price) is not float:
                raise TypeError("Price must be a number")

            if price < 0:
                raise ValueError("Price cannot be negative")

            self.price = float(price)

        if 'latitude' in place_data:
            latitude = place_data['latitude']

            if type(latitude) is not int and type(latitude) is not float:
                raise TypeError("Latitude must be a number")

            if latitude < -90 or latitude > 90:
                raise ValueError("Invalid latitude")

            self.latitude = float(latitude)

        if 'longitude' in place_data:
            longitude = place_data['longitude']

            if type(longitude) is not int and type(longitude) is not float:
                raise TypeError("Longitude must be a number")

            if longitude < -180 or longitude > 180:
                raise ValueError("Invalid longitude")

            self.longitude = float(longitude)
