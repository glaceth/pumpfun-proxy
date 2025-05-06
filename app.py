from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/api/pump", methods=["GET"])
def get_pump_tokens():
    try:
        url = "https://api.pumpfunapi.org/pumpfun/new/tokens"
        response = requests.get(url)
        data = response.json()

        # On retourne les 5 tokens les plus récents
        return jsonify(data[:5])
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
