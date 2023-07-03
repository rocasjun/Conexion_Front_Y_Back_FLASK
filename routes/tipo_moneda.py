from flask import Blueprint, request, jsonify
from models.tipo_moneda import Tipo_Moneda
from utils.db import db

tipo_moneda = Blueprint('tipo_moneda', __name__, url_prefix='/api/tipo_moneda')