from flask import Blueprint, request, jsonify
from models.recibo_estado import Recibo_Estado
from utils.db import db

recibo_estado = Blueprint('recibo_estado', __name__, url_prefix='/api/recibo_estado')