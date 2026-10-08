classDiagram
class User {
    +UUID id
    +String first_name
    +String last_name
    +String email
    +String password
    +DateTime created_at
    +DateTime updated_at
    +register()
    +update_profile()
}

class Place {
    +UUID id
    +String title
    +String description
    +Float price
    +Float latitude
    +Float longitude
    +DateTime created_at
    +DateTime updated_at
    +create()
    +update()
    +delete()
}

class Review {
    +UUID id
    +String text
    +Integer rating
    +DateTime created_at
    +DateTime updated_at
    +create()
    +update()
    +delete()
}

class Amenity {
    +UUID id
    +String name
    +String description
    +DateTime created_at
    +DateTime updated_at
    +create()
    +update()
    +delete()
}

User "1" --> "0..*" Place : owns
User "1" --> "0..*" Review : writes
Place "1" --> "0..*" Review : has
Place "0..*" --> "0..*" Amenity : includes