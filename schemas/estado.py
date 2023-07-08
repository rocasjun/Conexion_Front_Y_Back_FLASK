from utils.ma import ma
from models.estado import Estado

class EstadoSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Estado
        fields = ['id_estado', 'descripcion']


tipo_estado_schema = EstadoSchema()
tipo_estados_schema = EstadoSchema(many=True)