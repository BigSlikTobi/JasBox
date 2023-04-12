import json
from flask_cors import CORS
from flask import Flask, jsonify, request

app = Flask(__name__)
CORS(app) # Add this line to enable CORS

@app.route('/select-device', methods=['POST'])
def select_device():
    data = request.get_json()

    # Save selected device data to selected_device.json
    with open('selected_device.json', 'w') as f:
        json.dump(data, f)

    return jsonify({'message': 'Device selected'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000, debug=True)
