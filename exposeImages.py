from flask import Flask, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app) # Add this line to enable CORS

@app.route('/images')
def images():
    with open('images.json') as f:
        images_data = json.load(f)
    images = images_data['devices']
    return jsonify(images)

if __name__ == '__main__':
    app.run(debug=True, port=4002)
