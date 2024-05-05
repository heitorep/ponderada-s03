from flask import Blueprint, jsonify
from services.zoologico_services import ZoologicoService

zoologico_route_bp = Blueprint('zoologico_route_bp', __name__)
zoologico_service = ZoologicoService()

@zoologico_route_bp.route('/zoologico/info', methods=['GET'])
def obter_informacoes_zoologico():
    info = zoologico_service.obter_info()
    return jsonify(info), 200
