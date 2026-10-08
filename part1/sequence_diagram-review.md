sequenceDiagram
  participant User
  participant API
  participant BusinessLogic
  participant Database
  participant User

User->>API: Submit Review
API->>BusinessLogic: create Review 
BusinessLogic->>Database: Save Review
Database-->>BusinessLogic: Confirm Review saved
BusinessLogic-->>API: Return Review information
API-->>User: Return Success/Failure
