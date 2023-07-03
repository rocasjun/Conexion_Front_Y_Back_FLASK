from dataclasses import dataclass

from utils.db import db


@dataclass
class Gasto(db.Model):

    __tablename__ = 'gasto'

    id_gasto = db.Column(db.Integer, primary_key = True)
    id_tipo_gasto = db.Column(db.Integer, db.ForeignKey('tipo_gasto.id_tipo_gasto'))
    descripcion = db.Column(db.String(100))

    recibo_detalle = db.relationship('Recibo_Detalle', backref='gasto')

    def __init__(self, id_tipo_gasto, descripcion):
        self.id_tipo_gasto = id_tipo_gasto
        self.descripcion = descripcion
