from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route('/devices')
def devices():
    with open('devices.json') as f:
        devices_data = json.load(f)
    devices = devices_data['devices']
    return jsonify(devices)

if __name__ == '__main__':
    app.run(debug=True, port=4001)

