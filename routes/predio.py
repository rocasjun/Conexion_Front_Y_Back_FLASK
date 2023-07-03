from flask import Blueprint, request, jsonify
from models.predio import Predio
from schemas.predio import predios_schema
from utils.db import db

predio = Blueprint('predio', __name__, url_prefix='/api/predios')

@predio.route("/", methods=['GET'])
def getPredios():
    predios = Predio.query.all()
    result = predios_schema.dump(predios)

    data = {
        "message": "ok",
        "status": 200,
        "predios": result
    }

    return jsonify(data)

@predio.route("/add", methods=['POST'])
def addPredio():
    body = request.get_json()

    nombre = body['nombre']
    direccion = body['direccion']
    distrito = body['distrito']
    telefono = body['telefono']
    id_tipo_predio = body['id_tipo_predio']
    print(nombre, direccion)

    nuevo_predio = Predio(nombre, direccion, distrito, telefono, id_tipo_predio)
    db.session.add(nuevo_predio)
    db.session.commit()

    return "saving a new condo"