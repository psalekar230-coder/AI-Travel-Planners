from flask import Flask, render_template, request, jsonify
import firebase_admin
from firebase_admin import credentials, firestore, auth

app = Flask(__name__)

# Firebase Admin SDK connect - tuzya firebase cha json file ithe tak
# cred = credentials.Certificate("ai-travel-planner-c2026-firebase-adminsdk.json")
# firebase_admin.initialize_app(cred)
# db = firestore.client()

@app.route('/')
def home():
    return render_template('index.html')  # tuzha html file templates folder madhe thev

@app.route('/get_trip_plan', methods=['POST'])
def get_trip_plan():
    data = request.json
    destination = data['destination']
    trip_type = data['type']  # couple, family, friends
    
    # AI logic - simple demo
    plans = {
        "goa": {
            "couple": "Romantic beach dinner + Sunset cruise at Baga",
            "family": "Beach + Dolphin trip + Fort Aguada visit",
            "friends": "Nightlife + Water sports + Party at Anjuna"
        },
        "manali": {
            "couple": "Snow point + Couple photoshoot at Solang",
            "family": "Hadimba Temple + Solang Valley + Kullu",
            "friends": "Paragliding + Trekking + Campfire"
        }
    }
    
    plan = plans.get(destination.lower(), {}).get(trip_type, "Plan not available")
    return jsonify({"plan": plan})

if __name__ == '__main__':
    app.run(debug=True)