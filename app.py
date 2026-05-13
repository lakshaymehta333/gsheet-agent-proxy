from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)

APPS_SCRIPT_URL = "https://script.google.com/a/macros/bystadium.com/s/AKfycbyN-FMZ_tL-os7xF9pjE-oV0IqLuHBLYJGQGK0xwTgWbl5HeBKRb61fw-9eqcj9C0JK/exec"

@app.route("/")
def home():
    return jsonify({"status": "running"})

@app.route("/sheet", methods=["GET"])
def get_sheet():
    action = request.args.get("action", "getColumns")

    try:
        response = requests.get(
            APPS_SCRIPT_URL,
            params={"action": action},
            allow_redirects=True,
            timeout=30
        )

        try:
            data = response.json()
        except Exception:
            data = json.loads(response.text)

        return jsonify(data)

    except Exception as e:
        return jsonify({
            "error": "Proxy failed",
            "details": str(e)
        }), 500
