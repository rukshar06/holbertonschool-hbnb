#!/usr/bin/python3

from flask_restx import Namespace, Resource, fields
from services import facade

api = Namespace('places', description='Place operations')

# Models for related entities
amenity_model = api.model('PlaceAmenity', {
    'id': fields.String(description='Amenity ID'),
    'name': fields.String(description='Name of the amenity')
})

user_model = api.model('PlaceUser', {
    'id': fields.String(description='User ID'),
    'first_name': fields.String(description='First name of the owner'),
    'last_name': fields.String(description='Last name of the owner'),
    'email': fields.String(description='Email of the owner')
})

review_model = api.model('PlaceReview', {
    'id': fields.String(description='Review ID'),
    'text': fields.String(description='Text of the review'),
    'rating': fields.Integer(description='Rating of the place (1-5)'),
    'user_id': fields.String(description='ID of the user')
})

# Input model for creating a place
place_model = api.model('Place', {
    'title': fields.String(required=True, description='Title of the place'),
    'description': fields.String(description='Description of the place'),
    'price': fields.Float(required=True, description='Price per night'),
    'latitude': fields.Float(required=True, description='Latitude of the place'),
    'longitude': fields.Float(required=True, description='Longitude of the place'),
    'owner_id': fields.String(required=True, description='ID of the owner'),
    'amenities': fields.List(fields.String, required=True,
                             description="List of amenity IDs")
})

# Input model for updating a place
place_update_model = api.model('PlaceUpdate', {
    'title': fields.String(description='Title of the place'),
    'description': fields.String(description='Description of the place'),
    'price': fields.Float(description='Price per night'),
    'latitude': fields.Float(description='Latitude of the place'),
    'longitude': fields.Float(description='Longitude of the place'),
    'owner_id': fields.String(description='ID of the owner'),
    'amenities': fields.List(fields.String, description='List of amenity IDs')
})


def place_to_dict(place):
    """Convert a place object into a dictionary."""

    return {
        'id': place.id,
        'title': place.title,
        'description': place.description,
        'price': place.price,
        'latitude': place.latitude,
        'longitude': place.longitude,
        'owner': {
            'id': place.owner.id,
            'first_name': place.owner.first_name,
            'last_name': place.owner.last_name,
            'email': place.owner.email
        },
        'amenities': [
            {
                'id': amenity.id,
                'name': amenity.name
            }
            for amenity in place.amenities
        ],
        'reviews': [
            {
                'id': review.id,
                'text': review.text,
                'rating': review.rating,
                'user_id': review.user.id
            }
            for review in place.reviews
        ]
    }


@api.route('/')
class PlaceList(Resource):

    @api.expect(place_model, validate=True)
    @api.response(201, 'Place successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new place."""

        place_data = api.payload

        try:
            place = facade.create_place(place_data)
        except (ValueError, TypeError) as error:
            return {'error': str(error)}, 400

        return place_to_dict(place), 201

    @api.response(200, 'List of places retrieved successfully')
    def get(self):
        """Retrieve a list of all places."""

        places = facade.get_all_places()

        return [
            place_to_dict(place)
            for place in places
        ], 200


@api.route('/<place_id>')
class PlaceResource(Resource):

    @api.response(200, 'Place details retrieved successfully')
    @api.response(404, 'Place not found')
    def get(self, place_id):
        """Get place details by ID."""

        place = facade.get_place(place_id)

        if not place:
            return {'error': 'Place not found'}, 404

        return place_to_dict(place), 200

    @api.expect(place_update_model, validate=True)
    @api.response(200, 'Place updated successfully')
    @api.response(404, 'Place not found')
    @api.response(400, 'Invalid input data')
    def put(self, place_id):
        """Update a place's information."""

        place_data = api.payload

        try:
            place = facade.update_place(place_id, place_data)
        except (ValueError, TypeError) as error:
            return {'error': str(error)}, 400

        if not place:
            return {'error': 'Place not found'}, 404

        return place_to_dict(place), 200


# Reviews route from the original scaffold
@api.route('/<place_id>/reviews')
class PlaceReviewList(Resource):

    @api.response(200, 'List of reviews for the place retrieved successfully')
    @api.response(404, 'Place not found')
    def get(self, place_id):
        """Get all reviews for a specific place."""

        place = facade.get_place(place_id)

        if not place:
            return {'error': 'Place not found'}, 404

        return [], 200
