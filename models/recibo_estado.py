from dataclasses import dataclass

from utils.db import db


@dataclass
class Recibo_Estado(db.Model):

    __tablename__ = 'recibo_estado'

    id_recibo_estado = db.Column(db.Integer, primary_key = True)
    descripcion = db.Column(db.String(15))

    recibo = db.relationship('Recibo', backref='estado_recibo')

    def __init__(self, nombre):
        self.descripcion = nombre

    def to_json(self):
        return {
            "id": self.id_recibo_estado,
            "nombre": self.descripcion
        }