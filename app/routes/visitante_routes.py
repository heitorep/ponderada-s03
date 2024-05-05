from flask import Blueprint, jsonify, request
from services.visitante_services import VisitanteService

visitante_route_bp = Blueprint('visitante_route_bp', __name__)
visitante_service = VisitanteService()

@visitante_route_bp.route('/visitantes', methods=['POST'])
def criar_visitante():
    data = request.json
    nome = data.get('nome')
    idade = data.get('idade')
    
    if nome is None or idade is None:
        return jsonify({'error': 'Dados incompletos'}), 400
    
    visitante = visitante_service.criar_visitante(nome, idade)
    return jsonify({'message': 'Visitante criado com sucesso', 'visitante': visitante.__dict__}), 201

@visitante_route_bp.route('/visitantes', methods=['GET'])
def obter_visitantes():
    visitantes = visitante_service.listar_visitantes()
    return jsonify([visitante.__dict__ for visitante in visitantes]), 200
