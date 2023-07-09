from utils.db import db
from dataclasses import dataclass

@dataclass
class Cuenta(db.Model):

    __tablename__ = 'cuenta'

    id_cuenta = db.Column(db.Integer, primary_key = True)
    ncuenta = db.Column(db.BigInteger)
    id_tipo_moneda = db.Column(db.Integer, db.ForeignKey('tipo_moneda.id_tipo_moneda'))
    id_persona = db.Column(db.Integer, db.ForeignKey('persona.id_persona'))
    id_banco = db.Column(db.Integer, db.ForeignKey('banco.id_banco'))

    recaudacion = db.relationship('Recaudacion', backref='cuenta_origen_recaudacion')

    def __init__(self, id_persona, id_banco, id_tipo_moneda, ncuenta):
        self.ncuenta = ncuenta
        self.id_tipo_moneda = id_tipo_moneda
        self.id_persona = id_persona
        self.id_banco = id_banco

    def to_json(self):
        return {
            "id": self.id_cuenta,
            "numero_cuenta": self.ncuenta,
            "id_tipo_moneda": self.id_tipo_moneda,
            "id_persona": self.id_persona,
            "id_banco": self.id_banco
        }