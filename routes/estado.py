from flask import Blueprint, request, jsonify
from models.estado import Estado
from utils.db import db

estado = Blueprint('estado', __name__, url_prefix='/api/estado')