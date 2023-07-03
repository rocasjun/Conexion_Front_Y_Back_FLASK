from dataclasses import dataclass

from utils.db import db


@dataclass
class Banco(db.Model):

    __tablename__ = 'banco'

    id_banco = db.Column(db.Integer, primary_key = True)
    descripcion = db.Column(db.String(50))

    cuentas = db.relationship('Cuenta', backref='banco')
    cuentas_predio = db.relationship('Cuenta_Predio', backref='banco_predio')

    def __init__(self, nombre):
        self.descripcion = nombre

    def to_json(self):
        return {
            "id": self.id_banco,
            "nombre": self.descripcion
        }