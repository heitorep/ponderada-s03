import unittest
from flask import Flask
from app.models.animal import Animal
from app.models.recinto import Recinto
from app.models.visitante import Visitante
from app.models.zoologico import Zoologico
from app.routes.animal_routes import animal_route_bp
from app.routes.recinto_routes import recinto_route_bp
from app.routes.visitante_routes import visitante_route_bp
from app.routes.zoologico_routes import zoologico_route_bp
from app.services.animal_services import AnimalService
from app.services.recinto_services import RecintoService
from app.services.visitante_services import VisitanteService
from app.services.zoologico_services import ZoologicoService

class TestZooSystem(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(animal_route_bp)
        self.app.register_blueprint(recinto_route_bp)
        self.app.register_blueprint(visitante_route_bp)
        self.app.register_blueprint(zoologico_route_bp)
        self.client = self.app.test_client()

        self.animal_service = AnimalService()
        self.recinto_service = RecintoService()
        self.visitante_service = VisitanteService()
        self.zoologico_service = ZoologicoService()

    def test_system_workflow(self):
        # Criar um animal
        with self.app.test_request_context(json={'nome': 'Mufasa', 'especie': 'Leão', 'felicidade': 50}):
            self.animal_service.criar_animal('Mufasa', 'Leão', 50)

        # Criar um recinto e adicionar um animal
        recinto = self.recinto_service.criar_recinto('Savana', 'Leão', 'Bem cuidado')
        self.recinto_service.adicionar_animal_recinto('Savana', Animal('Leo', 'Leão', 50))

        # Criar um visitante e registrar uma visita
        self.visitante_service.criar_visitante('Xuxa Meneguel', 28)
        self.visitante_service.registrar_visita_visitante('Xuxa Meneguel')

        # Testar se o sistema registra corretamente a receita e as visitas
        self.zoologico_service.registrar_visita_receita(1, 20)  # Suponha que cada visita custe 20

        # Verificar informações do zoológico
        info = self.zoologico_service.obter_info()
        self.assertEqual(info['total_visitas'], 1)
        self.assertEqual(info['receita_total'], 20)
        self.assertEqual(len(info['recintos']), 1)

if __name__ == '__main__':
    unittest.main()
