from flask import Blueprint, jsonify, request, make_response

from models.persona import Persona
from schemas.persona import persona_schema, personas_schema
from utils.db import db

persona = Blueprint('persona', __name__, url_prefix='/api/persona')

# @persona.route("/", methods=['GET'])
# def getPersonas():
#     data = {}
#     personas = Persona.query.all()
#     data['Personas'] = [persona.to_json() for persona in personas]

#     print(personas)  

#     return jsonify(data)

@persona.route("/", methods=['GET'])
def getPersonas():
    
    personas = Persona.query.all()
    result = personas_schema.dump(personas)

    personas = {
        'message': 'All Persons',
        'status': 200,
        'personas': result
    }

    return jsonify(personas)

@persona.route("/add", methods=['POST'])
def addPersona():
    body = request.get_json()

    apellido_paterno = body['apellido_paterno']
    apellido_materno = body['apellido_materno']
    nombres = body['nombres']
    fecha_nacimiento = body['fecha_nacimiento']
    id_tipo_documento = body['id_tipo_documento']
    numero_documento = body['numero_documento']
    direccion = body['direccion']
    idubigeo = body['idubigeo']

    nueva_persona = Persona(apellido_paterno, apellido_materno, nombres, fecha_nacimiento, id_tipo_documento, numero_documento, direccion, idubigeo)
    db.session.add(nueva_persona)
    db.session.commit()

    return "saving a new person"