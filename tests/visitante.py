import unittest
from app.services.visitante_services import VisitanteService

class TestVisitante(unittest.TestCase):
    def setUp(self):
        self.visitante_service = VisitanteService()
        self.visitante_service.criar_visitante("Tiaguinho", 30)

    def test_registrar_visita(self):
        self.visitante_service.registrar_visita_visitante("Tiaguinho")
        visitantes = self.visitante_service.listar_visitantes()
        self.assertEqual(visitantes[0].visitas, 1)

    def test_registrar_gasto(self):
        self.visitante_service.registrar_gasto_visitante("Tiaguinho", 100)
        visitantes = self.visitante_service.listar_visitantes()
        self.assertEqual(visitantes[0].dinheiro_gasto, 100)

if __name__ == '__main__':
    unittest.main()
