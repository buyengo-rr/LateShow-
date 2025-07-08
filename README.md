# lateshow-yourname

## Setup

- Clone the repository
- Install dependencies: `pip install -r requirements.txt`
- Run migrations: `flask db init`, `flask db migrate`, `flask db upgrade`
- Seed the database as required

## Endpoints

- GET /episodes
- GET /episodes/<id>
- GET /guests
- POST /appearances

## Model Relationships

- Episode has many Guests through Appearance
- Guest has many Episodes through Appearance
- Appearance belongs to Guest and Episode

## Validations

- Appearance.rating must be between 1 and 5 inclusive
