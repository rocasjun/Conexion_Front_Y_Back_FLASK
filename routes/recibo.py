import datetime

from flask import Blueprint, jsonify, request
from sqlalchemy import text

from models.recibo import Recibo
from models.recibo_detalle import Recibo_Detalle
from models.gasto import Gasto
from models.tipo_gasto import Tipo_Gasto

from schemas.recibo import recibos_schema
from schemas.recibo_detalle import detalle_recibos_schema

from utils.db import db

recibos = Blueprint('recibo', __name__, url_prefix='/api/recibos')

@recibos.route("/", methods=['GET'])
def getRecibos():
    recibos = Recibo.query.all()
    result = recibos_schema.dump(recibos)

    data = {
        "recibos": result
    }

    return jsonify(data)

@recibos.route("/add", methods=['POST'])
def addRecibo():
    body = request.get_json()

    numero_recibo = body['numero_recibo']
    periodo = body['periodo']
    fecha_vencimiento = datetime.datetime.strptime(body['fecha_vencimiento'], "%d/%m/%Y")
    fecha_emision = datetime.datetime.strptime(body['fecha_emision'], "%d/%m/%Y")
    importe = body['importe']
    ajuste = body['ajuste']
    observacion = body['observacion']
    id_casa = body['id_casa']
    id_recibo_estado = body['id_recibo_estado']

    nuevo_recibo = Recibo(numero_recibo, periodo,fecha_emision, fecha_vencimiento, importe, ajuste, observacion, id_casa, id_recibo_estado)
    db.session.add(nuevo_recibo)
    db.session.commit()

    return "saving a new receipt"

@recibos.route("/detalle/", methods=['GET'])
def listarRecibosDetalle():
    recibos = Recibo_Detalle.query.all()
    result = detalle_recibos_schema.dump(recibos)

    data = {
        "detalle-recibos": result
    }

    return jsonify(data)

@recibos.route("/detalle/<int:id>", methods=['GET'])
def listarDetallesRecibo(id):
    detalles_recibos = Recibo_Detalle.query.filter(Recibo_Detalle.id_mant_recibo == id).all()
    result = detalle_recibos_schema.dump(detalles_recibos)

    data = {
        "detalles-recibo": result
    }

    return jsonify(data)

@recibos.route("/recibo-tipo-gasto/<int:id>", methods=['GET'])
def mantenimientoReciboTipoGasto(id):
    detalle_recibos = (
        Recibo_Detalle.query
        .join(Gasto, Recibo_Detalle.id_gasto == Gasto.id_gasto)
        .join(Tipo_Gasto, Gasto.id_tipo_gasto == Tipo_Gasto.id_tipo_gasto)
        .filter(Recibo_Detalle.id_mant_recibo == id)
        .all()
    )
    result = detalle_recibos_schema.dump(detalle_recibos)

    datos_agrupados = {}

    for item in result:
        descripcion = item["gasto"]["tipo_gasto"]["descripcion"]
        importe = float(item["importe_casa"])

        datos_agrupados[descripcion] = importe if descripcion not in datos_agrupados else (datos_agrupados[descripcion] + importe)

    data = [
        {"descripcion": descripcion, "total_tipo_gasto": importe}
        for descripcion, importe in datos_agrupados.items()
    ]

    return jsonify(data)