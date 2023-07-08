from utils.ma import ma
from models.predio import Predio
from schemas.tipo_predio import TipoPredioSchema
#from schemas.cuenta_predio import CuentaPredioSchema

class PredioSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Predio
        fields = ['id_predio', 'descripcion', 'ruc', 'telefono', 'correo', 'direccion', 'idubigeo', 'tipo_predio']

    tipo_predio = ma.Nested(TipoPredioSchema, only=['nomre_predio'])
    #cuentas_predio = ma.Nested(CuentaPredioSchema, many=True, only=["ncuenta", "ntarjeta"])


predio_schema = PredioSchema()
predios_schema = PredioSchema(many=True)