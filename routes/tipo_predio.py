from flask import Blueprint, request, jsonify
from models.tipo_predio import Tipo_Predio
from utils.db import db

tipo_predio = Blueprint('tipo_predio', __name__, url_prefix='/api/tipo_predio')