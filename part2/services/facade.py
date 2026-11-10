#!/usr/bin/python3
"""Define the HBnB Facade."""

from persistence.repository import InMemoryRepository
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBnBFacade:
    """Facade for managing HBnB operations."""

    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()

    # USER METHODS

    def create_user(self, user_data):
        user = User(**user_data)
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        return self.user_repo.get(user_id)

    def update_user(self, user_id, user_data):
        user = self.user_repo.get(user_id)

        if not user:
            return None

        user.update(user_data)
        return user

    def get_user_by_email(self, email):
        return self.user_repo.get_by_attribute('email', email)

    def get_all_users(self):
        return self.user_repo.get_all()

    # AMENITY METHODS

    def create_amenity(self, amenity_data):
        amenity = Amenity(**amenity_data)
        self.amenity_repo.add(amenity)
        return amenity

    def get_amenity(self, amenity_id):
        return self.amenity_repo.get(amenity_id)

    def get_all_amenities(self):
        return self.amenity_repo.get_all()

    def update_amenity(self, amenity_id, amenity_data):
        amenity = self.amenity_repo.get(amenity_id)

        if not amenity:
            return None

        amenity.update(amenity_data)
        return amenity

    # PLACE METHODS

    def create_place(self, place_data):
        place_data = place_data.copy()

        owner_id = place_data.pop('owner_id')
        amenities_ids = place_data.pop('amenities', [])

        owner = self.user_repo.get(owner_id)

        if not owner:
            raise ValueError("Owner not found")

        place = Place(owner=owner, **place_data)

        for amenity_id in amenities_ids:
            amenity = self.amenity_repo.get(amenity_id)

            if not amenity:
                raise ValueError("Amenity not found")

            place.add_amenity(amenity)

        self.place_repo.add(place)
        return place

    def get_place(self, place_id):
        return self.place_repo.get(place_id)

    def get_all_places(self):
        return self.place_repo.get_all()

    def update_place(self, place_id, place_data):
        place = self.place_repo.get(place_id)

        if not place:
            return None

        place_data = place_data.copy()

        if 'owner_id' in place_data:
            owner_id = place_data.pop('owner_id')
            owner = self.user_repo.get(owner_id)

            if not owner:
                raise ValueError("Owner not found")

            place.owner = owner

        if 'amenities' in place_data:
            amenities_ids = place_data.pop('amenities')
            place.amenities = []

            for amenity_id in amenities_ids:
                amenity = self.amenity_repo.get(amenity_id)

                if not amenity:
                    raise ValueError("Amenity not found")

                place.add_amenity(amenity)

        place.update(place_data)
        return place

    # REVIEW METHODS

    def create_review(self, review_data):
        review_data = review_data.copy()

        user_id = review_data.pop('user_id')
        place_id = review_data.pop('place_id')

        user = self.user_repo.get(user_id)
        place = self.place_repo.get(place_id)

        if not user:
            raise ValueError("User not found")

        if not place:
            raise ValueError("Place not found")

        review = Review(user=user, place=place, **review_data)

        self.review_repo.add(review)
        place.add_review(review)

        return review

    def get_review(self, review_id):
        return self.review_repo.get(review_id)

    def get_all_reviews(self):
        return self.review_repo.get_all()

    def get_reviews_by_place(self, place_id):
        place = self.place_repo.get(place_id)

        if not place:
            return None

        return place.reviews

    def update_review(self, review_id, review_data):
        review = self.review_repo.get(review_id)

        if not review:
            return None

        review.update(review_data)
        return review

    def delete_review(self, review_id):
        review = self.review_repo.get(review_id)

        if not review:
            return False

        review.place.reviews.remove(review)
        self.review_repo.delete(review_id)

        return True
