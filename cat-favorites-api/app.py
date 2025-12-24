from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

favorites = []

CAT_API_URL = "http://cat-api:5000/cats"

@app.route("/favorites", methods=["GET"])
def get_favorites():
    return jsonify(favorites)

@app.route("/favorites", methods=["POST"])
def add_favorite():
    data = request.json

    # Cat API'ye sor (mikroservis iletişimi)
    cat_response = requests.get(CAT_API_URL)
    if cat_response.status_code != 200:
        return jsonify({"error": "Cat API erişilemiyor"}), 500

    favorites.append(data)
    return jsonify({"message": "Favoriye eklendi", "data": data}), 201

@app.route("/favorites/<cat_id>", methods=["DELETE"])
def delete_favorite(cat_id):
    global favorites
    favorites = [f for f in favorites if str(f["id"]) != cat_id]

    return jsonify({"message": "Favori silindi"})
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
