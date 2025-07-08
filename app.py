from flask import Flask, request, jsonify
from flask_migrate import Migrate
from models import db, Episode, Guest, Appearance

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lateshow.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)
@app.route('/episodes', methods=['GET'])
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([{"id": e.id, "date": e.date, "number": e.number} for e in episodes])


@app.route('/episodes/<int:id>', methods=['GET'])
def get_episode(id):
    episode = Episode.query.get(id)
    if not episode:
        return jsonify({"error": "Episode not found"}), 404
    return jsonify({
        "id": episode.id,
        "date": episode.date,
        "number": episode.number,
        "appearances": [
            {
                "id": a.id,
                "rating": a.rating,
                "guest_id": a.guest_id,
                "episode_id": a.episode_id,
                "guest": a.guest.to_dict()
            } for a in episode.appearances
        ]
    })


@app.route('/guests', methods=['GET'])
def get_guests():
    guests = Guest.query.all()
    return jsonify([g.to_dict() for g in guests])
@app.route('/appearances', methods=['POST'])
def create_appearance():
    data = request.json
    rating = data.get("rating")
    episode_id = data.get("episode_id")
    guest_id = data.get("guest_id")
    if not (1 <= rating <= 5):
        return jsonify({"errors": ["validation errors"]}), 400
    episode = Episode.query.get(episode_id)
    guest = Guest.query.get(guest_id)
    if not episode or not guest:
        return jsonify({"errors": ["validation errors"]}), 400
    appearance = Appearance(rating=rating, episode_id=episode_id, guest_id=guest_id)
    db.session.add(appearance)
    db.session.commit()
    return jsonify(appearance.to_dict()), 201


if __name__ == '__main__':
    app.run()

