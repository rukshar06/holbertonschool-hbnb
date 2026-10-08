classDiagram
    class PresentationLayer {
        +Services
        +API
    }

    <<Interface>> PresentationLayer
    class BusinessLogicLayer {
    +user
    +Place
    +Review
    +Amenity
}
class PersistenceLayer {
    +DatabaseAccess
    +Repositories
}
PresentationLayer --> BusinessLogicLayer : Facade Pattern
BusinessLogicLayer --> PersistenceLayer : Database Operations
