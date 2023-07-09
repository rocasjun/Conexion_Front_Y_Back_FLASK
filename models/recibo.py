from dataclasses import dataclass
from datetime import datetime

from utils.db import db


@dataclass
class Recibo(db.Model):

    __tablename__ = 'mant_recibo'

    id_mant_recibo = db.Column(db.Integer, primary_key = True)
    id_casa = db.Column(db.Integer, db.ForeignKey('casa.id_casa'))
    n_recibo = db.Column(db.String(50))
    periodo = db.Column(db.String(50))
    fecha_emision = db.Column(db.DateTime)
    fecha_vencimiento = db.Column(db.DateTime)
    importe = db.Column(db.Float(10,2))
    ajuste = db.Column(db.Float(6,2))
    observacion = db.Column(db.String(100))
    id_recibo_estado = db.Column(db.Integer, db.ForeignKey('recibo_estado.id_recibo_estado'))

    recaudacion = db.relationship('Recaudacion', backref='recibo_mant_recaudacion')

    def __init__(self, numero_recibo, periodo, fecha_emision, fecha_vencimiento, importe, ajuste, observacion, id_casa, id_recibo_estado):
        self.n_recibo = numero_recibo
        self.periodo = periodo
        self.fecha_emision = fecha_emision
        self.fecha_vencimiento = fecha_vencimiento
        self.importe = importe
        self.ajuste = ajuste
        self.observacion = observacion
        self.id_casa = id_casa
        self.id_recibo_estado = id_recibo_estado

    def to_json(self):
        return {
            "id": self.id_mant_recibo,
            "numero_recibo": self.n_recibo,
            "periodo": self.periodo,
            "fecha_emision": datetime.strftime(self.fecha_emision, '%d/%m/%Y'),
            "fecha_vencimiento": datetime.strftime(self.fecha_vencimiento, '%d/%m/%Y'),
            "importe": self.importe,
            "ajuste": self.ajuste,
            "observacion": self.observacion,
            "id_casa": self.id_casa,
            "id_recibo_estado": self.id_recibo_estado
        }