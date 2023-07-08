from utils.ma import ma
from models.casa import Casa

from schemas.predio_mdu import PredioMduSchema

class CasaSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Casa
        fields = [
            "id_casa",
            "numero",
            "piso",
            "area",
            "participacion",
            "predio_mdu"
        ]
    
    predio_mdu = ma.Nested(PredioMduSchema)

casa_schema = CasaSchema()
casas_schema = CasaSchema(many=True)