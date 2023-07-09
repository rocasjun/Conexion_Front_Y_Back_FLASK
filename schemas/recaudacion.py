from utils.ma import ma
from models.recaudacion import Recaudacion
from schemas.recaudacion_estado import RecaudacionEstadoSchema
from schemas.cuenta_predio import CuentaPredioSchema
from schemas.cuenta import CuentaSchema
from schemas.recibo import ReciboSchema
from schemas.tipo_moneda import TipoMonedaSchema

class RecaudacionSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Recaudacion
        fields = [
            "id_recaudacion",
            "n_operacion",
            "fecha_operacion",
            "moneda_recaudacion",
            "importe",
            "observacion",
            "estado_recaudacion",
            "cuenta_predio_recaudacion",
            "cuenta_origen_recaudacion",
            "recibo_mant_recaudacion",
            "predio_mdu"
        ]
    
    estado_recaudacion = ma.Nested(RecaudacionEstadoSchema, only=['descripcion'])
    cuenta_predio_recaudacion = ma.Nested(CuentaPredioSchema, only=["ncuenta"])
    cuenta_origen_recaudacion = ma.Nested(CuentaSchema, only=['ncuenta', 'persona'])
    recibo_mant_recaudacion = ma.Nested(ReciboSchema, only=["id_mant_recibo", "n_recibo", "periodo", "importe", "ajuste", "casa"])
    moneda_recaudacion = ma.Nested(TipoMonedaSchema, )

recaudacion_schema = RecaudacionSchema()
recaudaciones_schema = RecaudacionSchema(many=True)