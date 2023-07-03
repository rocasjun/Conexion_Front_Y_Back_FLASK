from flask import Blueprint, request, jsonify
from models.cuenta import Cuenta
from schemas.cuenta import cuenta_schema, cuentas_schema
from utils.db import db

cuenta = Blueprint('cuenta', __name__, url_prefix='/api/cuenta')

# @cuenta.route("/", methods=['GET'])
# def getCuentas():
#     data = {}
#     cuentas = Cuenta.query.all()
#     data['Cuentas'] = [cuenta.to_json() for cuenta in cuentas]

#     print(cuentas)  

#     return jsonify(data)


@cuenta.route("/", methods=['GET'])
def getCuentas():
    print("inicio")
    cuentas = Cuenta.query.all()
    print(cuentas) 
    result = cuentas_schema.dump(cuentas)

    data = {
        'message': 'Todas las cuentas',
        'status': 200,
        'cuentas': result
    } 

    return jsonify(data)


@cuenta.route("/add", methods=['POST'])
def addCuentas():
    body = request.get_json()
    
    numero_cuenta = body['ncuenta']
    moneda = body['id_tipo_moneda']
    id_persona = body['id_persona']
    id_banco = body['id_banco']

    nueva_cuenta = Cuenta(id_persona, id_banco, moneda, numero_cuenta)
    db.session.add(nueva_cuenta)
    db.session.commit()

    return "saving a new account"