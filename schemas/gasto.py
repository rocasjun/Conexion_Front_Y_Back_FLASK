from utils.ma import ma
from models.gasto import Gasto
from schemas.tipo_gasto import TipoGastoSchema

class GastoSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Gasto
        fields = [
            "id_gasto",
            "id_tipo_gasto",
            "descripcion",
            "tipo_gasto"
        ]

    tipo_gasto = ma.Nested(TipoGastoSchema, only=['descripcion'])
        

tipo_gasto_schema = GastoSchema()
tipo_gastos_schema = GastoSchema(many=True)