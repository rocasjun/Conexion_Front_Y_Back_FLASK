from dataclasses import dataclass

from utils.db import db


@dataclass
class Casa(db.Model):

    __tablename__ = 'casa'

    id_casa = db.Column(db.Integer, primary_key = True)
    id_predio = db.Column(db.Integer, db.ForeignKey('predio.id_predio'))
    id_estado = db.Column(db.Integer, db.ForeignKey('casa_estado.id_estado'))
    id_predio_mdu = db.Column(db.Integer, db.ForeignKey('predio_mdu.id_predio_mdu'))
    numero = db.Column(db.Integer)
    piso = db.Column(db.Integer)
    area = db.Column(db.Float(10,2))
    participacion = db.Column(db.Float(6,2))

    recibo = db.relationship('Recibo', backref='casa')

    def __init__(self, id_casa, id_predio, id_estado, id_predio_mdu, numero, piso, area, participacion):
        self.id_casa = id_casa
        self.id_predio = id_predio
        self.id_estado = id_estado
        self.id_predio_mdu = id_predio_mdu
        self.numero = numero
        self.piso = piso
        self.area = area
        self.participacion = participacion

    def to_json(self):
        return {
            "id_casa": self.id_casa,
            "id_predio": self.id_predio,
            "id_estado": self.id_estado,
            "id_predio_mdu": self.id_predio_mdu,
            "numero": self.numero,
            "piso": self.piso,
            "area": self.area,
            "participacion": self.participacion
        }