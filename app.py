from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

APPS_SCRIPT_URL = "https://script.google.com/macros/s/AKfycbzHupevl6AyWd_hi9dK3W5t5i2jjZA4TzBk7BiRooytbchneUvXLML4vY72G3970Alv/exec"

@app.route("/")
def home():
    return jsonify({"status": "running"})

@app.route("/sheet", methods=["GET"])
def get_sheet():

    action = request.args.get("action", "getColumns")

    response = requests.get(
        APPS_SCRIPT_URL,
        params={"action": action},
        allow_redirects=True,
        timeout=30
    )

    return response.text, 200, {
        "Content-Type": "application/json"
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
