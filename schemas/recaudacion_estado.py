from utils.ma import ma
from models.recaudacion_estado import Recaudacion_Estado

class RecaudacionEstadoSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Recaudacion_Estado
        fields = ['id_recaudacion_estado', 'descripcion']

recaudacion_estado = RecaudacionEstadoSchema()
recaudaciones_estado = RecaudacionEstadoSchema(many=True)