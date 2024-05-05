from flask import Blueprint, jsonify, request
from services.animal_services import AnimalService

animal_route_bp = Blueprint('animal_route_bp', __name__)
animal_service = AnimalService()

@animal_route_bp.route('/animais', methods=['POST'])
def criar_animal():
    data = request.json
    nome = data.get('nome')
    especie = data.get('especie')
    felicidade = data.get('felicidade')
    
    if nome is None or especie is None or felicidade is None:
        return jsonify({'error': 'Dados incompletos'}), 400
    
    animal = animal_service.criar_animal(nome, especie, felicidade)
    return jsonify({'message': 'Animal criado com sucesso', 'animal': animal.__dict__}), 201

@animal_route_bp.route('/animais', methods=['GET'])
def obter_animais():
    animais = animal_service.listar_animais()
    return jsonify([animal.__dict__ for animal in animais]), 200

@animal_route_bp.route('/animais/alimentar', methods=['POST'])
def alimentar_animal():
    data = request.json
    nome = data.get('nome')
    
    if not nome:
        return jsonify({'error': 'Nome do animal é necessário'}), 400

    if animal_service.alimentar_animal(nome):
        return jsonify({'message': f'{nome} foi alimentado com sucesso.'}), 200
    return jsonify({'error': 'Animal não encontrado'}), 404
