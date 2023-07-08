from utils.ma import ma
from models.tipo_documento import Tipo_Documento

class TipoDocumentoSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Tipo_Documento
        fields = ['id_tipo_documento', 'descripcion']


documento_persona_schema = TipoDocumentoSchema()