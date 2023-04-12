from flask import Flask, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app) # Add this line to enable CORS

@app.route('/devices')
def devices():
    with open('devices.json') as f:
        devices_data = json.load(f)
    devices = devices_data['devices']
    return jsonify(devices)

if __name__ == '__main__':
    app.run(debug=True, port=4001)
