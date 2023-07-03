from utils.db import db
from dataclasses import dataclass

@dataclass
class Predio_Mdu(db.Model):

    __tablename__ = 'predio_mdu'

    id_predio_mdu = db.Column(db.Integer, primary_key = True)
    id_predio = db.Column(db.Integer, db.ForeignKey('predio.id_predio'))
    id_mdu = db.Column(db.Integer, db.ForeignKey('mdu.id_mdu'))
    descripcion = db.Column(db.String(4))
    direccion = db.Column(db.String(10))
    numero = db.Column(db.String(10))

    casa = db.relationship('Casa', backref='predio_mdu')


    def __init__(self, id_predio, id_mdu, descripcion, direccion, numero):
        self.descripcion = descripcion
        self.id_predio = id_predio
        self.id_mdu = id_mdu
        self.direccion = direccion
        self.numero = numero
