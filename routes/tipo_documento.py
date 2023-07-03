from flask import Blueprint, request, jsonify
from models.tipo_documento import Tipo_Documento
from utils.db import db

tipo_documento = Blueprint('tipo_documento', __name__, url_prefix='/api/tipo_documento')