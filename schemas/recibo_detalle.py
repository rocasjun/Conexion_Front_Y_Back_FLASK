from utils.ma import ma
from models.recibo_detalle import Recibo_Detalle
from schemas.gasto import GastoSchema

class ReciboDetalleSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Recibo_Detalle
        fields = [
            "id_mant_recibo_det",
            "id_mant_recibo",
            "gasto",
            "importe_casa"
        ]

    gasto = ma.Nested(GastoSchema, only=["id_gasto", "descripcion", "tipo_gasto"])
        

detalle_recibo_schema = ReciboDetalleSchema()
detalle_recibos_schema = ReciboDetalleSchema(many=True)