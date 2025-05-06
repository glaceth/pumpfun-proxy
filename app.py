from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/api/pump", methods=["GET"])
def get_tokens():
    try:
        url = "https://pump.fun/api/token/list?sort=recent"
        headers = {
            "User-Agent": "Mozilla/5.0",
            "Accept": "application/json"
        }
        response = requests.get(url, headers=headers)
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
