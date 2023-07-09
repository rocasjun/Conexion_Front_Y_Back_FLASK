from utils.ma import ma
from models.recibo_estado import Recibo_Estado

class ReciboEstadoSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Recibo_Estado
        fields = [
            "id_recibo_estado",
            "descripcion"
        ]

rebico_casa_schema = ReciboEstadoSchema()
rebicos_casa_schema = ReciboEstadoSchema(many=True)