from utils.ma import ma
from models.cuenta import Cuenta
from schemas.persona import PersonaSchema
from schemas.banco import BancoSchema
from schemas.tipo_moneda import TipoMonedaSchema

class CuentaSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Cuenta
        fields = ['id_cuenta', 'ncuenta', 'moneda_cuenta', 'persona', 'banco']

    moneda_cuenta = ma.Nested(TipoMonedaSchema, only=['descripcion', 'etiqueta'])
    persona = ma.Nested(PersonaSchema, only=['nombres', 'apellido_paterno', 'apellido_materno', 'ndocumento'])
    banco = ma.Nested(BancoSchema, only=['descripcion'])


cuenta_schema = CuentaSchema()
cuentas_schema = CuentaSchema(many=True)