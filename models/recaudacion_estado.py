from dataclasses import dataclass

from utils.db import db


@dataclass
class Recaudacion_Estado(db.Model):

    __tablename__ = 'recaudacion_estado'

    id_recaudacion_estado = db.Column(db.Integer, primary_key = True)
    descripcion = db.Column(db.String(15))

    recaudacion = db.relationship('Recaudacion', backref='estado_recaudacion')

    def __init__(self, nombre):
        self.descripcion = nombre

    def to_json(self):
        return {
            "id": self.id_recaudacion_estado,
            "nombre": self.descripcion
        }