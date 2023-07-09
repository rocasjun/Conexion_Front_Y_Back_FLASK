from dataclasses import dataclass

from utils.db import db


@dataclass
class Tipo_Documento(db.Model):

    __tablename__ = 'tipo_documento'

    id_tipo_documento = db.Column(db.Integer, primary_key = True)
    descripcion = db.Column(db.String(20))

    def __init__(self, nombres):
        self.descripcion = nombres

    def to_json(self):
        return {
            "id": self.id,
            "nombre": self.descripcion
        }