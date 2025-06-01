from flask import Flask,jsonify
from datetime import datetime
import socket

app = Flask(__name__)

@app.route('/api/v1/details')
def details():
    return jsonify({
        "hostname": socket.gethostname(),
        "datetime": datetime.now().isoformat()
    })

@app.route('/api/v1/healthz')
def healthz():
    return jsonify({
        "status": "up"
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0')