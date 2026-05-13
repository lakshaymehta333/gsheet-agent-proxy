from flask import Flask, request, jsonify
import requests
import json
import traceback

app = Flask(__name__)

APPS_SCRIPT_URL = "https://script.google.com/macros/s/AKfycbzHupevl6AyWd_hi9dK3W5t5i2jjZA4TzBk7BiRooytbchneUvXLML4vY72G3970Alv/exec"

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
