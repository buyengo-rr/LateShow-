from app import app, db
from models import Episode, Guest, Appearance

def seed_data():
    with app.app_context():
        Appearance.query.delete()
        Episode.query.delete()
        Guest.query.delete()
        db.session.commit()

        episodes = [
            Episode(date="2025-06-01", number=1),
            Episode(date="2025-06-08", number=2),
            Episode(date="2025-06-15", number=3),
        ]
        db.session.add_all(episodes)
        db.session.commit()

        guests = [
            Guest(name="Alice Johnson", occupation="Comedian"),
            Guest(name="Bob Smith", occupation="Musician"),
            Guest(name="Carol Lee", occupation="Actor"),
        ]
        db.session.add_all(guests)
        db.session.commit()

        appearances = [
            Appearance(rating=4, episode_id=episodes[0].id, guest_id=guests[0].id),
            Appearance(rating=5, episode_id=episodes[0].id, guest_id=guests[1].id),
            Appearance(rating=3, episode_id=episodes[1].id, guest_id=guests[2].id),
            Appearance(rating=5, episode_id=episodes[2].id, guest_id=guests[0].id),
        ]
        db.session.add_all(appearances)
        db.session.commit()

        print("Database seeded successfully!")

if __name__ == "__main__":
    seed_data()
