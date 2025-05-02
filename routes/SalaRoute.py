from flask import Blueprint, request, jsonify
from models.SalaModel import SalaModel
from database import db

sala_bp = Blueprint('sala', __name__)

@sala_bp.route('/salas', methods=['GET'])
def listar_salas():
    salas = SalaModel.query.all()
    return jsonify([sala.to_dict() for sala in salas]), 200

@sala_bp.route('/salas/<int:sala_id>', methods=['GET'])
def obter_sala(sala_id):
    sala = SalaModel.query.get(sala_id)
    if sala:
        return jsonify(sala.to_dict()), 200
    return jsonify({'message': 'Sala não encontrada'}), 404

@sala_bp.route('/salas', methods=['POST'])
def criar_sala(): 
    data = request.get_json()
    nova_sala = SalaModel(
        nome=data.get('nome'),
        localizacao=data.get('localizacao'),
        capacidade=data.get('capacidade'),
        tipo=data.get('tipo'),
        recursos=data.get('recursos'),
        disponivel=data.get('disponivel', True)
    )

    db.session.add(nova_sala)
    db.session.commit()
    return jsonify(nova_sala.to_dict()), 201

@sala_bp.route('/salas/<int:sala_id>', methods=['PUT'])
def atualizar_sala(sala_id):
    sala = SalaModel.query.get(sala_id)
    if not sala:
        return jsonify({'message': 'Sala não encontrada'}), 404

    data = request.get_json()
    sala.nome = data.get('nome', sala.nome)
    sala.localizacao = data.get('localizacao', sala.localizacao)
    sala.capacidade = data.get('capacidade', sala.capacidade)
    sala.tipo = data.get('tipo', sala.tipo)
    sala.recursos = data.get('recursos', sala.recursos)
    sala.disponivel = data.get('disponivel', sala.disponivel)

    db.session.commit()
    return jsonify(sala.to_dict()), 200

@sala_bp.route('/salas/<int:sala_id>', methods=['DELETE'])
def deletar_sala(sala_id):
    sala = SalaModel.query.get(sala_id)
    if not sala:
        return jsonify({'message': 'Sala não encontrada'}), 404

    db.session.delete(sala)
    db.session.commit()
    return jsonify({'message': 'Sala deletada com sucesso'}), 200

