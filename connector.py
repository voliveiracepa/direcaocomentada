from pymongo import MongoClient


def get_database(an):
    client = MongoClient('mongodb+srv://voliveira:FgeWAmJhW29aYBiF@direcaocomentada.nlwaoo3.mongodb.net/?retryWrites=true&w=majority&appName=direcaocomentada')
    return client[an]
