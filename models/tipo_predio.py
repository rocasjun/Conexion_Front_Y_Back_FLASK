from dataclasses import dataclass

from utils.db import db


@dataclass
class Tipo_Predio(db.Model):

    __tablename__ = 'tipo_predio'

    id_tipo_predio = db.Column(db.Integer, primary_key = True)
    nomre_predio = db.Column(db.String(50))

    tipo_predio = db.relationship('Predio', backref='tipo_predio', lazy=True)

    def __init__(self, nombre):
        self.nomre_predio = nombre

    def to_json(self):
        return {
            "id": self.id_tipo_predio,
            "nombre": self.nomre_predio
        }