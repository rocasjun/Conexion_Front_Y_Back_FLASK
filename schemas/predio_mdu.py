from utils.ma import ma
from models.predio_mdu import Predio_Mdu

class PredioMduSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Predio_Mdu
        fields = [
            "id_predio_mdu",
            "id_predio",
            "id_mdu",
            "descripcion",
            "direccion",
            "numero"
        ]
        

predio_mdu_schema = PredioMduSchema()
predios_mdu_schema = PredioMduSchema(many=True)