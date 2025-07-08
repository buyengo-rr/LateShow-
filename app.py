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

