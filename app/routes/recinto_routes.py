from flask import Blueprint, jsonify, request
from services.recinto_services import RecintoService
from services.animal_services import AnimalService  # Precisamos disso para adicionar animais aos recintos

recinto_route_bp = Blueprint('recinto_route_bp', __name__)
recinto_service = RecintoService()
animal_service = AnimalService()  # Instância para interagir com o serviço de animais

@recinto_route_bp.route('/recintos', methods=['POST'])
def criar_recinto():
    data = request.json
    nome = data.get('nome')
    especie = data.get('especie')
    estado_cuidado = data.get('estado_cuidado')
    
    if nome is None or especie is None or estado_cuidado is None:
        return jsonify({'error': 'Dados incompletos'}), 400
    
    recinto = recinto_service.criar_recinto(nome, especie, estado_cuidado)
    return jsonify({'message': 'Recinto criado com sucesso', 'recinto': recinto.__dict__}), 201

@recinto_route_bp.route('/recintos', methods=['GET'])
def obter_recintos():
    recintos = recinto_service.listar_recintos()
    return jsonify([recinto.__dict__ for recinto in recintos]), 200
