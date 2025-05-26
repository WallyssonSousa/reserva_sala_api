from flask import Blueprint, request, jsonify
from models.ReservaModel import ReservaModel
from models.SalaModel import SalaModel
from database import db
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from datetime import datetime, timedelta
from services.GestaoEscolarService import professor_existe, turma_existe

reserva_bp = Blueprint('reserva', __name__)
def tem_confiltos(sala_id, horario_inicio, horario_fim, reserva_id=None):
    conflitos = ReservaModel.query.filter(
        ReservaModel.sala_id == sala_id,
        ReservaModel.id != reserva_id,
        ReservaModel.horario_inicio < horario_fim,
        ReservaModel.horario_fim > horario_inicio
    ).first()
    return conflitos is not None

@reserva_bp.route('/reservas', methods=['GET'])
def obter_reservas():
    reservas = ReservaModel.query.all()
    return jsonify([r.to_dict() for r in reservas]), 200

@reserva_bp.route('/reservas/<int:reserva_id>', methods=['GET'])
def obter_reserva(reserva_id):
    reserva = ReservaModel.query.get_or_404(reserva_id)
    return jsonify(reserva.to_dict()), 200

@reserva_bp.route('/reservas', methods=['POST'])
@jwt_required()
def criar_reserva():
    jwt_claims = get_jwt()
    if jwt_claims.get("role") != "admin":
        return jsonify({"erro": "Acesso negado: apenas administradores podem criar reservas."}), 403
    
    data = request.get_json()

    try: 
        inicio = datetime.fromisoformat(data['horario_inicio'])
        fim = datetime.fromisoformat(data['horario_fim'])
    except (ValueError, KeyError):
        return jsonify({'message': 'Formato de data inválido ou faltando'}), 400
    
    if not professor_existe(data['professor_id']):
        return jsonify({'message': 'Professor não encontrado'}), 404
    
    if not turma_existe(data['turma_id']):
        return jsonify({'message': 'Turma não encontrada'}), 404
    
    if fim <= inicio:
        return jsonify({'message': 'O horário de fim deve ser maior que o horário de início'}), 400
    
    if tem_confiltos(data['sala_id'], inicio, fim):
        return jsonify({'message': 'Conflito de horário para a sala'}), 409
    
    nova_reserva = ReservaModel(
        sala_id=data['sala_id'],
        horario_inicio=inicio,
        horario_fim=fim,
        professor_id=data['professor_id'],
        turma_id=data['turma_id']
    )

    db.session.add(nova_reserva)
    db.session.commit()

    return jsonify(nova_reserva.to_dict()), 201

@reserva_bp.route('/reservas/<int:reserva_id>', methods=['PUT'])
@jwt_required()
def atualizar_reserva(id):
    jwt_claims = get_jwt()
    if jwt_claims.get("role") != "admin":
        return jsonify({"erro": "Acesso negado: apenas administradores podem atualizar reservas."}), 403
    
    reserva = ReservaModel.query.get_or_404(id)
    data = request.get_json()

    try:
        inicio = datetime.fromisoformat(data['horario_inicio'])
        fim = datetime.fromisoformat(data['horario_fim'])
    except (ValueError, KeyError):
        return jsonify({'message': 'Formato de data inválido ou faltando'}), 400
    
    if fim <= inicio:
        return jsonify({'message': 'O horário de fim deve ser maior que o horário de início'}), 400
    
    if tem_confiltos(data['sala_id'], inicio, fim, reserva.id):
        return jsonify({'message': 'Conflito de horário para a sala'}), 409
    
    required_fields = ['sala_id', 'horario_inicio', 'horario_fim', 'professor_id', 'turma_id']
    missing = [f for f in required_fields if f not in data]

    if missing:
        return jsonify({'message': f'Campos obrigatórios faltando: {", ".join(missing)}'}), 400
    
    reserva.sala_id = data['sala_id']
    reserva.horario_inicio = inicio
    reserva.horario_fim = fim
    reserva.professor_id = data['professor_id']
    reserva.turma_id = data['turma_id']

    db.session.commit()
    return jsonify(reserva.to_dict()), 200

@reserva_bp.route('/reservas/<int:reserva_id>', methods=['DELETE'])
@jwt_required()
def deletar_reserva(id):
    jwt_claims = get_jwt()
    if jwt_claims.get("role") != "admin":
        return jsonify({"erro": "Acesso negado: apenas administradores podem deletar reservas."}), 403
    
    reserva = ReservaModel.query.get_or_404(id)
    db.session.delete(reserva)
    db.session.commit()
    return jsonify({'message': 'Reserva deletada com sucesso'}), 200
