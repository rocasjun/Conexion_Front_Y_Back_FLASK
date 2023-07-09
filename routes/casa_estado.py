from flask import Blueprint, request, jsonify
from models.casa_estado import Casa_Estado
from utils.db import db

casa_estado = Blueprint('casa_estado', __name__, url_prefix='/api/casa_estado')