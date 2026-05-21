from flask import Flask, jsonify

app = Flask(__name__)

users = {
    1: {"name": "Alice", "email": "alice@example.com"}
}

@app.route("/users/<int:user_id>")
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=False)