from flask import Flask, jsonify
import requests

app = Flask(__name__)

CAT_API_URL = "https://catfact.ninja/fact"

@app.route("/cats", methods=["GET"])
def get_cat_fact():
    response = requests.get(CAT_API_URL)
    data = response.json()

    return jsonify({
        "id": data.get("length"),   # basit unique değer
        "fact": data.get("fact")
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
