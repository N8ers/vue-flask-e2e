from flask import Flask, jsonify, Response
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)

mock_data = [
    {"name": "value A"},
    {"name": "value B"},
    {"name": "value C"},
    {"name": "value D"},
    {"name": "value E"},
]


@app.route("/hello")
def say_hello():
    response = {"data": "Hello"}
    return jsonify(response)


@app.route("/data", methods=["GET"])
def get_data():
    response = {"data": mock_data}
    return jsonify(response)
