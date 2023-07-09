from utils.ma import ma
from models.tipo_autorizacion import Tipo_Autorizacion

class TipoAutorizacionSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Tipo_Autorizacion
        fields = ['id_tipo_autorizacion', 'descripcion']


tipo_autorizacion_schema = TipoAutorizacionSchema()
tipo_autorizaciones_schema = TipoAutorizacionSchema(many=True)