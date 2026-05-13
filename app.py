from flask import Flask, request, jsonify
import requests
import json
import traceback

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

        return jsonify({
            "status_code": response.status_code,
            "final_url": response.url,
            "content_type": response.headers.get("Content-Type"),
            "raw_text_first_500": response.text[:500]
        })

    except Exception as e:
        return jsonify({
            "error": str(e),
            "traceback": traceback.format_exc()
        }), 500
