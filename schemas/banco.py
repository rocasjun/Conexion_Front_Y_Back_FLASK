from utils.ma import ma
from models.banco import Banco

class BancoSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Banco
        fields = ['id_banco', 'descripcion']


banco_schema = BancoSchema()
bancos_schema = BancoSchema(many=True)