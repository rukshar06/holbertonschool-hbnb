sequenceDiagram
participant User
participant API
participant BusinessLogic
participant Database

User->>API: User Registration
API->>BusinessLogic: create User
BusinessLogic->>Database: Save User information
Database-->>BusinessLogic: Confirm User saved
BusinessLogic-->>API: Return User information
API-->>User: Return Success/Failure
