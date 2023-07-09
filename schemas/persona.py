from utils.ma import ma
from models.persona import Persona
from schemas.tipo_documento import TipoDocumentoSchema

class PersonaSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Persona
        fields = ['id_persona', 'nombres', 'apellido_paterno', 'apellido_materno', 'documento', 'ndocumento', 'direccion', 'idubigeo']

    documento = ma.Nested(TipoDocumentoSchema, only=['descripcion'])


persona_schema = PersonaSchema()
personas_schema = PersonaSchema(many=True)