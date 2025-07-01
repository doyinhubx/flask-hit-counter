from flask import Flask, jsonify, request

app = Flask(__name__)
counter = {"visits": 0}

@app.route("/", methods=["GET"])
def home():
    counter["visits"] += 1
    return jsonify(message=f"Hello, you’ve visited {counter['visits']} times!")

@app.route("/reset", methods=["POST"])
def reset():
    counter["visits"] = 0
    return jsonify(message="Counter reset.")

if __name__ == '__main__':
    app.run(debug=True)