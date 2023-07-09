from utils.ma import ma
from models.tipo_moneda import Tipo_Moneda

class TipoMonedaSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Tipo_Moneda
        fields = ['id_tipo_moneda', 'descripcion', 'etiqueta']


tipo_moneda_schema = TipoMonedaSchema()
tipo_monedas_schema = TipoMonedaSchema(many=True)