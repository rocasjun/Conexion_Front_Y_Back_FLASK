from flask import Blueprint, request, jsonify
from models.banco import Banco
from utils.db import db

banco = Blueprint('banco', __name__, url_prefix='/api/banco')