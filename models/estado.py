from dataclasses import dataclass

from utils.db import db


@dataclass
class Estado(db.Model):

    __tablename__ = 'estado'

    id_estado = db.Column(db.Integer, primary_key = True)
    descripcion = db.Column(db.String(15))

    cuentas_predio = db.relationship('Cuenta_Predio', backref='estado_cuenta_predio')

    def __init__(self, descripcion):
        self.descripcion = descripcion

    def to_json(self):
        return {
            "id": self.id_estado,
            "nombre": self.descripcion
        }