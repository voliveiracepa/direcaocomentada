from flask import Flask, jsonify, request
from flask_cors import CORS
from controller.routes import Routes

app = Flask(__name__)
CORS(app)

Routes(app)

if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0', debug=True)