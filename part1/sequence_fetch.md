sequenceDiagram

participant User
participant API
participant BusinessLogic
participant Database

User->>API: Request list of Places
API->>BusinessLogic: Search Places by criteria
BusinessLogic->>Database: Fetch matching Places
Database-->>BusinessLogic: Return list of Places
BusinessLogic-->>API: Return list of Places
API-->>User: Display list of Places
