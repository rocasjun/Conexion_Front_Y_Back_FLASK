from dataclasses import dataclass

from utils.db import db


@dataclass
class Tipo_Autorizacion(db.Model):

    __tablename__ = 'tipo_autorizacion'

    id_tipo_autorizacion = db.Column(db.Integer, primary_key = True)
    descripcion = db.Column(db.String(50))

    cuentas_predio = db.relationship('Cuenta_Predio', backref='autorizacion_cuenta_predio')

    def __init__(self, descripcion):
        self.descripcion = descripcion

    def to_json(self):
        return {
            "id": self.id_tipo_autorizacion,
            "nombre": self.descripcion
        }