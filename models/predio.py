from utils.db import db
from dataclasses import dataclass

@dataclass
class Predio(db.Model):

    __tablename__ = 'predio'

    id_predio = db.Column(db.Integer, primary_key = True)
    id_tipo_predio = db.Column(db.Integer, db.ForeignKey('tipo_predio.id_tipo_predio'))
    descripcion = db.Column(db.String(100))
    ruc = db.Column(db.String(20))
    telefono = db.Column(db.String(10))
    correo = db.Column(db.String(80))
    direccion = db.Column(db.String(100))
    idubigeo = db.Column(db.String(6))

    #tipo_predio = db.relationship('Tipo_Predio', backref='tipo_predio', lazy=True)
    #cuentas_predio = db.relationship('Cuenta_Predio', back_populates='predio_relacionado')
    predio = db.relationship('Cuenta_Predio', backref='predio')

    def __init__(self, descripcion, ruc, telefono, correo, direccion, idubigeo, id_tipo_predio):
        self.descripcion = descripcion
        self.ruc = ruc
        self.correo = correo
        self.direccion = direccion
        self.idubigeo = idubigeo
        self.telefono = telefono
        self.id_tipo_predio = id_tipo_predio

    def to_json(self):
        return {
            "id": self.id_predio,
            "nombre": self.descripcion,
            "ruc": self.ruc,
            "correo": self.correo,
            "direccion": self.direccion,
            "distrito": self.idubigeo,
            "telefono": self.telefono,
            "id_tipo_predio": self.id_tipo_predio
        }