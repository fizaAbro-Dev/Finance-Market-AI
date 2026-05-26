from flask import Flask, render_template, jsonify
import json
import os

app = Flask(
    __name__,
    template_folder="../templates",
    static_folder="../static"
)

# -------------------------
# Home Route (Dashboard UI)
# -------------------------
@app.route("/")
def home():
    return render_template("index.html")


# -------------------------
# API Route (Send Data to Frontend)
# -------------------------
@app.route("/data")
def data():
    file_path = "prices.json"

    # If file doesn't exist, return empty data
    if not os.path.exists(file_path):
        return jsonify({"error": "prices.json not found"})

    with open(file_path, "r") as file:
        try:
            prices = json.load(file)
        except json.JSONDecodeError:
            prices = []

    return jsonify(prices)


# -------------------------
# Health Check Route
# -------------------------
@app.route("/status")
def status():
    return jsonify({"status": "running", "app": "Finance AI Agent"})


# -------------------------
# Run Server
# -------------------------
if __name__ == "__main__":
    print("🚀 Starting Finance AI Agent Server...")
    app.run(debug=True)