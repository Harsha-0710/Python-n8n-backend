from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/get-payload', methods=['POST'])
def get_payload():
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    data = request.get_json()

    if not data or "name" not in data:
        return jsonify({"error": "No 'name' field provided"}), 400
    
    name = data["name"]
    link = data["link"]
    updated_name = name + " - processed by Flask API"

    return jsonify({
        "message": "Payload received successfully",
        "link": link,
        "updated_name": updated_name
    }), 200


if __name__ == '__main__':
    app.run(debug=True)

