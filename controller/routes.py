from flask import jsonify, request
from connector import get_database

db = get_database('direcaocomentada')

collection = db['astrazeneca']

collection2 = db['astrazenecaNovo']

data = {
  "createdAt": "12/05/1990",
  "driver":{
    "name":"Jhson Doe",
    "email":"test@test.com",
    "corporationId":"15524",
    "birthDate":"12/05/1950",
    "joinDate":"12/05/1990"
  },
  "event": {
    "eventDate" : "12/05/1999",
    "eventTime": "08:00:00",
    "local":"Street123",
    "UF": "SP",
    "isWorking":"sim",
    "isMyFault": "nao",
    "ADLCall":"123"
  },
  "roadCondictions":{
    "illumination":"escuro",
    "roadType":"em bom estado",
    "type":"seco"
  }
}
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
            collection2.insert_one(value_from_front)

            return jsonify({"message": "Dados recebidos e salvos com sucesso!"}), 200
        except Exception as e:
            return jsonify({"error": e}), 500
    def online(self):
        return 'server on'

