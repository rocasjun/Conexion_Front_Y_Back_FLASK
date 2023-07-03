from dataclasses import dataclass

from utils.db import db


@dataclass
class Tipo_Gasto(db.Model):

    __tablename__ = 'tipo_gasto'

    id_tipo_gasto = db.Column(db.Integer, primary_key = True)
    id_clase_gasto = db.Column(db.Integer, db.ForeignKey('clase_gasto.id_clase_gasto'))
    descripcion = db.Column(db.String(100))

    gasto = db.relationship('Gasto', backref='tipo_gasto')

    def __init__(self, id_clase_gasto, descripcion):
        self.id_clase_gasto = id_clase_gasto
        self.descripcion = descripcion
