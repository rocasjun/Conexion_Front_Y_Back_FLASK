from utils.ma import ma
from models.tipo_gasto import Tipo_Gasto

class TipoGastoSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Tipo_Gasto
        fields = [
            "id_tipo_gasto",
            "id_clase_gasto",
            "descripcion"
        ]
        

tipo_gasto_schema = TipoGastoSchema()
tipo_gastos_schema = TipoGastoSchema(many=True)