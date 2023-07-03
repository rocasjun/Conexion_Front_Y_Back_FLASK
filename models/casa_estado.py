from dataclasses import dataclass

from utils.db import db


@dataclass
class Casa_Estado(db.Model):

    __tablename__ = 'casa_estado'

    id_estado = db.Column(db.Integer, primary_key = True)
    descripcion = db.Column(db.String(15))

    def __init__(self, descripcion):
        self.descripcion = descripcion

    def to_json(self):
        return {
            "id": self.id_estado,
            "descripcion": self.descripcion
        }