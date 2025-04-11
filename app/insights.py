from flask import jsonify
from . import mongo
from collections import Counter

def generate_insights():
    entries = list(mongo.db.entries.find())

    if not entries:
        return jsonify({"message": "No health data found."}), 404

    total_sleep = sum(float(e.get("sleep_hours", 0)) for e in entries)
    total_hydration = sum(float(e.get("hydration_oz", 0)) for e in entries)
    total_exercise = sum(float(e.get("exercise_mins", 0)) for e in entries)
    moods = [str(e.get("mood", "unknown")).lower() for e in entries]

    mood_counts = dict(Counter(moods))
    count = len(entries)

    insights = {
        "entry_count": count,
        "average_sleep_hours": round(total_sleep / count, 2),
        "total_hydration_oz": total_hydration,
        "average_exercise_mins": round(total_exercise / count, 2),
        "mood_distribution": mood_counts
    }

    return jsonify(insights), 200
