from flask import Blueprint, request, jsonify
from models.tipo_autorizacion import Tipo_Autorizacion
from utils.db import db

tipo_autorizacion = Blueprint('tipo_autorizacion', __name__, url_prefix='/api/tipo_autorizacion')