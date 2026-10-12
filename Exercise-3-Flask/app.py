from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the Flash Sale App!"

@app.route("/buy")
def buy():
    return jsonify({"message": "Purchase successful!", "status": "success"})

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)