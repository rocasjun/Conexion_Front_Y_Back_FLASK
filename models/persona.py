from dataclasses import dataclass

from utils.db import db


@dataclass
class Persona(db.Model):

    __tablename__ = 'persona'

    id_persona = db.Column(db.Integer, db.Sequence('id_persona_seq'), primary_key = True)
    nombres = db.Column(db.String(50), nullable=False)
    apellido_paterno = db.Column(db.String(50), nullable=False)
    apellido_materno = db.Column(db.String(50), nullable=False)
    id_tipo_documento = db.Column(db.Integer, db.ForeignKey('tipo_documento.id_tipo_documento'))
    ndocumento = db.Column(db.String(20), nullable=False)
    fecha_nacimiento = db.Column(db.DateTime, nullable=False)
    direccion = db.Column(db.String(150), nullable=False)
    idubigeo = db.Column(db.String(6), nullable=False)

    documento = db.relationship('Tipo_Documento', backref='documento')
    #persona_cuentas = db.relationship('Cuenta', backref='persona_cuenta', lazy=True)
    cuentas = db.relationship('Cuenta', backref='persona')

    def __init__(self, apellido_paterno, apellido_materno, nombres, fecha_nacimiento, id_tipo_documento, numero_documento, direccion, idubigeo):
        self.nombres = nombres
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.fecha_nacimiento = fecha_nacimiento
        self.id_tipo_documento = id_tipo_documento
        self.ndocumento = numero_documento
        self.direccion = direccion
        self.idubigeo = idubigeo

    def to_json(self):
        return {
            "id": self.id_persona,
            "nombres": self.nombres,
            "apellido_paterno": self.apellido_paterno,
            "apellido_materno": self.apellido_materno,
            "fecha_nacimiento": self.fecha_nacimiento,
            "id_tipo_documento": self.id_tipo_documento,
            "numero_documento": self.ndocumento,
            "direccion": self.direccion,
            "idubigeo": self.idubigeo
        }