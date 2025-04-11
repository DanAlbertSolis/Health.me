from flask import Blueprint, request, jsonify
from . import mongo
from .insights import generate_insights

healthme = Blueprint("healthme", __name__)

@healthme.route("/entries", methods=["POST"])
@healthme.route("/entries", methods=["POST"])
def add_entry():
    data = request.get_json()

    required_fields = ["date", "sleep_hours", "hydration_oz", "exercise_mins", "mood"]
    missing = [field for field in required_fields if field not in data]

    if missing:
        return jsonify({"error": f"Missing fields: {', '.join(missing)}"}), 400

    try:
        entry = {
            "date": data["date"],
            "sleep_hours": float(data["sleep_hours"]),
            "hydration_oz": float(data["hydration_oz"]),
            "exercise_mins": int(data["exercise_mins"]),
            "mood": str(data["mood"])
        }
    except ValueError:
        return jsonify({"error": "Invalid data types. Please check your inputs."}), 400

    result = mongo.db.entries.insert_one(entry)
    return jsonify({"message": "Entry added", "entry_id": str(result.inserted_id)}), 201


@healthme.route("/entries", methods=["GET"])
def get_entries():
    entries = mongo.db.entries.find()
    result = []

    for entry in entries:
        result.append({
            "id": str(entry["_id"]),
            "date": entry.get("date"),
            "sleep_hours": entry.get("sleep_hours"),
            "hydration_oz": entry.get("hydration_oz"),
            "exercise_mins": entry.get("exercise_mins"),
            "mood": entry.get("mood")
        })

    return jsonify(result), 200

@healthme.route("/insights", methods=["GET"])
def insights():
    return generate_insights()
