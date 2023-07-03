from flask import Flask

from config import URI
from routes.predio import predio
from routes.cuenta import cuenta
from routes.tipo_moneda import tipo_moneda
from routes.cuenta_predio import cuenta_predio
from routes.casa import casa
from routes.persona import persona
from routes.recaudacion_estado import recaudacion_estado
from routes.recaudacion import recaudaciones
from routes.estado import estado
from routes.tipo_autorizacion import tipo_autorizacion
from routes.recibo import recibos
from routes.tipo_predio import tipo_predio
from routes.banco import banco
from routes.casa_estado import casa_estado
from routes.tipo_documento import tipo_documento
from routes.recibo_estado import recibo_estado
from utils.db import db
from utils.ma import ma

app = Flask(__name__)
# connection = psycopg2.connect(url)
app.config["SQLALCHEMY_DATABASE_URI"] = URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app.register_blueprint(persona)
app.register_blueprint(predio)
app.register_blueprint(casa)
app.register_blueprint(cuenta)
app.register_blueprint(tipo_moneda)
app.register_blueprint(cuenta_predio)
app.register_blueprint(recibos)
app.register_blueprint(recaudacion_estado)
app.register_blueprint(recaudaciones)
app.register_blueprint(estado)
app.register_blueprint(tipo_autorizacion)
app.register_blueprint(tipo_predio)
app.register_blueprint(banco)
app.register_blueprint(casa_estado)
app.register_blueprint(tipo_documento)
app.register_blueprint(recibo_estado)


db.init_app(app)
ma.init_app(app)