from flask import Blueprint, request, jsonify
from models.recaudacion_estado import Recaudacion_Estado
from utils.db import db

recaudacion_estado = Blueprint('recaudacion_estado', __name__, url_prefix='/api/recaudacion_estado')