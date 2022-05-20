from flask import Flask, jsonify, Response

app = Flask(__name__)

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
