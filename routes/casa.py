from flask import Blueprint, jsonify, request

from models.casa import Casa
from utils.db import db

casa = Blueprint('casa', __name__, url_prefix='/api/casa')

@casa.route("/", methods=['GET'])
def getCasas():
    data = {}
    casas = Casa.query.all()
    data['Casas'] = [casa.to_json() for casa in casas]

    print(casas)  

    return jsonify(data)

@casa.route("/add", methods=['POST'])
def addCasa():
    body = request.get_json()

    piso = body['piso']
    bloque = body['bloque']
    numero = body['numero']
    area = body['area']
    id_predio = body['id_predio']
    id_propietario = body['id_propietario']
    id_estado_casa = body["id_estado_casa"]

    nueva_casa = Casa(piso, bloque, numero, area, id_predio, id_propietario, id_estado_casa)
    db.session.add(nueva_casa)
    db.session.commit()

    return "saving a new department"