from flask import jsonify, request
from connector import get_database

db = get_database('direcaocomentada')

collection = db['astrazeneca']

class Routes:
    def __init__(self, app):
        self.app = app
        self.set_routes()

    def set_routes(self):
        self.app.route('/savedc', methods=['POST'])(self.save)
        self.app.route('/', methods=['GET'])(self.online)

    def save(self):
        try:
            value_from_front = request.json
            collection.insert_one(value_from_front)

            return jsonify({"message": "Dados recebidos e salvos com sucesso!"}), 200
        except Exception as e:
            return jsonify({"error": e}), 500
    def online(self):
        return 'server on'

