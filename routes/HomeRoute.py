from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required

home_bp = Blueprint('home', __name__)

@home_bp.route('/', methods=['GET'])
@jwt_required()
def home():
    return jsonify({"message": "Bem-vindo ao sistema de reservas de salas!"}), 200
