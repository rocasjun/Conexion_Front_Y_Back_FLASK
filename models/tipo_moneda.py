from dataclasses import dataclass

from utils.db import db


@dataclass
class Tipo_Moneda(db.Model):

    __tablename__ = 'tipo_moneda'

    id_tipo_moneda = db.Column(db.Integer, primary_key = True)
    descripcion = db.Column(db.String(50))
    etiqueta = db.Column(db.String(4))

    cuentas = db.relationship('Cuenta', backref='moneda_cuenta')
    cuentas_predios = db.relationship('Cuenta_Predio', backref='moneda_cuenta_predio')
    recaudacion_moneda = db.relationship('Recaudacion', backref='moneda_recaudacion')

    def __init__(self, descripcion, etiqueta):
        self.descripcion = descripcion
        self.etiqueta = etiqueta

    def to_json(self):
        return {
            "id": self.id_tipo_moneda,
            "nombre": self.descripcion,
            "etiqueta": self.etiqueta
        }