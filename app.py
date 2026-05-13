from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

APPS_SCRIPT_URL = "https://script.google.com/a/macros/bystadium.com/s/AKfycbyN-FMZ_tL-os7xF9pjE-oV0IqLuHBLYJGQGK0xwTgWbl5HeBKRb61fw-9eqcj9C0JK/exec"

@app.route("/sheet", methods=["GET"])
def get_sheet():

    action = request.args.get("action", "getColumns")

    response = requests.get(
        APPS_SCRIPT_URL,
        params={"action": action},
        allow_redirects=True,
        timeout=30
    )

    return jsonify(response.json())

@app.route("/")
def home():
    return {"status": "running"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)