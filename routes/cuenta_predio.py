from flask import Blueprint, request, jsonify
from models.cuenta_predio import Cuenta_Predio
from schemas.cuenta_predio import cuenta_schema, cuentas_schema
from utils.db import db

cuenta_predio = Blueprint('cuenta_predio', __name__, url_prefix='/api/cuenta_predio')

# @cuenta_predio.route("/", methods=['GET'])
# def getCuentas():
#     data = {}
#     cuentas = Cuenta_Predio.query.all()
#     data['Cuentas'] = [cuenta.to_json() for cuenta in cuentas]

#     print(cuentas)  

#     return jsonify(data)

@cuenta_predio.route("/", methods=['GET'])
def getCuentas():
    print("iniciio")
    cuentas = Cuenta_Predio.query.all()
    print(cuentas)
    result = cuentas_schema.dump(cuentas)
    #data['Cuentas'] = [cuenta.to_json() for cuenta in cuentas]
 
    data = {
        'message': 'Todas las cuentas predio',
        'status': 200,
        'cuentas': result
    }

    return jsonify(data)

@cuenta_predio.route("/add", methods=['POST'])
def addCuentas():
    body = request.get_json()

    id_predio = body['id_predio']
    id_estado = body['id_estado']
    id_tipo_autorizacion = body['id_tipo_autorizacion']
    id_banco = body['id_banco']
    id_tipo_moneda = body['id_tipo_moneda']
    ncuenta = body['ncuenta']
    ntarjeta = body['ntarjeta']
    fecha_apertura = body['fecha_apertura']
    fecha_autorizacion = body['fecha_autorizacion']
    fecha_cierre = body['fecha_cierre']
    correo_autorizado = body['correo_autorizado']

    nueva_cuenta = Cuenta_Predio(id_predio, id_estado, 
                                 id_tipo_autorizacion, id_banco,
                                 id_tipo_moneda, ncuenta, ntarjeta,
                                 fecha_apertura, fecha_autorizacion,
                                 fecha_cierre, correo_autorizado)
    db.session.add(nueva_cuenta)
    db.session.commit()

    return "saving a new account"