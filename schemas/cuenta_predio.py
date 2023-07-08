from utils.ma import ma
from models.cuenta_predio import Cuenta_Predio
from schemas.predio import PredioSchema
from schemas.estado import EstadoSchema
from schemas.tipo_autorizacion import TipoAutorizacionSchema
from schemas.banco import BancoSchema
from schemas.tipo_moneda import TipoMonedaSchema


class CuentaPredioSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Cuenta_Predio
        fields = [
            "id_cuenta_predio",
            "predio",
            # "estado_cuenta_predio",
            # "autorizacion_cuenta_predio",
            # "banco_predio",
            # "moneda_cuenta_predio",
            "ncuenta",
            "ntarjeta",
            "fecha_apertura",
            "fecha_autorizacion",
            "fecha_cierre",
            "correo_autorizado",
        ]

        predio = ma.Nested(PredioSchema, only=['id_predio', 'descripcion', 'ruc'])
        # estado_cuenta_predio = ma.Nested(EstadoSchema, only=['descripcion'])
        # autorizacion_cuenta_predio = ma.Nested(TipoAutorizacionSchema, only=['descripcion'])
        # banco_predio = ma.Nested(BancoSchema, only=['descripcion'])
        # moneda_cuenta_predio = ma.Nested(TipoMonedaSchema, only=['descripcion', 'etiqueta'])


cuenta_schema = CuentaPredioSchema()
cuentas_schema = CuentaPredioSchema(many=True)