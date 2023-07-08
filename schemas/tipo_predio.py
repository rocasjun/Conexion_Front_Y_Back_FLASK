from utils.ma import ma
from models.tipo_predio import Tipo_Predio

class TipoPredioSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Tipo_Predio
        fields = ['id_tipo_predio', 'nomre_predio']


tipo_predio_schema = TipoPredioSchema()
tipo_predios_schema = TipoPredioSchema(many=True)