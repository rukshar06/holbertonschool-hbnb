sequenceDiagram
participant user
participant API
participant BusinessLogic
participant Database

User->>API: Create Place listing
API->>BusinessLogic: create Place
BusinessLogic->>Database: Save Place information
Database-->>BusinessLogic: Confirm Place saved
BusinessLogic-->>API: Return Place information
API-->>User: Return Success/Failure
