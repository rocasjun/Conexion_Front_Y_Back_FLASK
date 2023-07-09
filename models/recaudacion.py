from dataclasses import dataclass
from datetime import datetime

from utils.db import db


@dataclass
class Recaudacion(db.Model):

    __tablename__ = 'recaudacion'

    id_recaudacion = db.Column(db.Integer, primary_key = True)
    id_cuenta = db.Column(db.Integer, db.ForeignKey('cuenta.id_cuenta'))
    id_mant_recibo = db.Column(db.Integer, db.ForeignKey('mant_recibo.id_mant_recibo'))
    n_operacion = db.Column(db.String(25))
    fecha_operacion = db.Column(db.DateTime, nullable=False)
    id_tipo_moneda = db.Column(db.Integer, db.ForeignKey('tipo_moneda.id_tipo_moneda'))
    importe = db.Column(db.Float(10,2))
    id_recaudacion_estado = db.Column(db.Integer, db.ForeignKey('recaudacion_estado.id_recaudacion_estado'))
    id_cuenta_predio = db.Column(db.Integer, db.ForeignKey('cuenta_predio.id_cuenta_predio'))
    observacion = db.Column(db.String(100))

    def __init__(self, id_cuenta, id_mant_recibo, noperacion, fecha_operacion, moneda, 
                 importe, id_recaudacion_estado, id_cuenta_predio, observacion):
        #self.id_recaudacion = id_recaudacion
        self.id_cuenta = id_cuenta
        self.id_mant_recibo = id_mant_recibo
        self.n_operacion = noperacion
        self.fecha_operacion = fecha_operacion
        self.id_tipo_moneda = moneda
        self.importe = importe
        self.id_recaudacion_estado = id_recaudacion_estado
        self.id_cuenta_predio = id_cuenta_predio
        self.observacion = observacion

    def to_json(self):
        return {
            "id_recaudacion": self.id_recaudacion,
            "id_cuenta": self.id_cuenta,
            "id_mant_recibo": self.id_mant_recibo,
            "numero_operacion": self.n_operacion,
            "fecha_operacion": datetime.strftime(self.fecha_operacion, '%Y-%m-%d'),
            "moneda": self.id_tipo_moneda,
            "importe": self.importe,
            "id_recaudacion_estado": self.id_recaudacion_estado,
            "id_cuenta_predio": self.id_cuenta_predio,
            "observacion": self.observacion
        }