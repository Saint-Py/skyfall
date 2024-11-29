from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# In-memory storage for rooms
rooms = {}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/create-room", methods=["POST"])
def create_room():
    data = request.json
    room_id = data.get("room_id")

    if room_id in rooms:
        return jsonify({"error": "Room already exists!"}), 400

    rooms[room_id] = {"players": []}
    return jsonify({"message": f"Room {room_id} created!"}), 201

@app.route("/join-room/<room_id>", methods=["POST"])
def join_room(room_id):
    if room_id not in rooms:
        return jsonify({"error": "Room not found!"}), 404

    data = request.json
    player_name = data.get("player_name")
    rooms[room_id]["players"].append(player_name)
    return jsonify({"message": f"{player_name} joined room {room_id}!"}), 200

@app.route("/get-rooms", methods=["GET"])
def get_rooms():
    return jsonify({"rooms": rooms}), 200

if __name__ == "__main__":
    app.run(debug=True)
