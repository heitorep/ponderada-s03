import unittest
from app.services.zoologico_services import ZoologicoService
from app.models.recinto import Recinto

class TestZoologico(unittest.TestCase):
    def setUp(self):
        self.zoologico_service = ZoologicoService()

    def test_registrar_visitas_receita(self):
        self.zoologico_service.registrar_visita_receita(100, 5000)
        info = self.zoologico_service.obter_info()
        self.assertEqual(info["total_visitas"], 100)
        self.assertEqual(info["receita_total"], 5000)

    def test_adicionar_recinto(self):
        recinto = Recinto("Floresta", "Cobra", "Bem cuidado")
        self.zoologico_service.adicionar_recinto(recinto)
        info = self.zoologico_service.obter_info()
        self.assertEqual(info["recintos"], 1)

if __name__ == '__main__':
    unittest.main()
