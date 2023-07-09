from utils.db import db
from dataclasses import dataclass

@dataclass
class Cuenta_Predio(db.Model):

    __tablename__ = 'cuenta_predio'

    id_cuenta_predio = db.Column(db.Integer, db.Sequence('id_cuenta_predio_seq'), primary_key = True)
    id_predio = db.Column(db.Integer, db.ForeignKey('predio.id_predio'))
    id_estado = db.Column(db.Integer, db.ForeignKey('estado.id_estado'))
    id_tipo_autorizacion = db.Column(db.Integer, db.ForeignKey('tipo_autorizacion.id_tipo_autorizacion'))
    id_banco = db.Column(db.Integer, db.ForeignKey('banco.id_banco'))
    id_tipo_moneda = db.Column(db.Integer, db.ForeignKey('tipo_moneda.id_tipo_moneda'))
    ncuenta = db.Column(db.BigInteger)
    ntarjeta = db.Column(db.BigInteger)
    fecha_apertura = db.Column(db.DateTime, nullable=False)
    fecha_autorizacion = db.Column(db.DateTime, nullable=False)
    fecha_cierre = db.Column(db.DateTime, nullable=True)
    correo_autorizado = db.Column(db.String(40))

    recaudacion = db.relationship('Recaudacion', backref='cuenta_predio_recaudacion')

    def __init__(self, id_predio, id_estado, id_tipo_autorizacion, id_banco, id_tipo_moneda, 
                 ncuenta, ntarjeta, fecha_apertura, fecha_autorizacion, fecha_cierre, correo_autorizado):
        self.id_predio = id_predio
        self.id_estado = id_estado
        self.id_tipo_autorizacion = id_tipo_autorizacion
        self.id_banco = id_banco
        self.id_tipo_moneda = id_tipo_moneda
        self.ncuenta = ncuenta
        self.ntarjeta = ntarjeta
        self.fecha_apertura = fecha_apertura
        self.fecha_autorizacion = fecha_autorizacion
        self.fecha_cierre = fecha_cierre
        self.correo_autorizado = correo_autorizado

    def to_json(self):
        return {
            "id_cuenta_predio": self.id_cuenta_predio,
            "id_predio": self.id_predio,
            "id_estado": self.id_estado,
            "id_tipo_autorizadion": self.id_tipo_autorizacion,
            "id_banco": self.id_banco,
            "id_tipo_moneda": self.id_tipo_moneda,
            "numero_cuenta": self.ncuenta,
            "numero_tarjeta": self.ntarjeta,
            "fecha_apertura": self.fecha_apertura,
            "fecha_autorizacion": self.fecha_autorizacion,
            "fecha_cierre": self.fecha_cierre,
            "correo_autorizado": self.correo_autorizado
        }