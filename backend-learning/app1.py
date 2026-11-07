from os import name
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "HI GUYS ITS MY HOME PAGE"

@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    name = data.get("name")
    if name:
        return jsonify(data)
    else:
        return "Please provide your name to register."

if __name__ == "__main__":
    app.run(debug=True)