import unittest
from app.models.animal import Animal
from app.services.recinto_services import RecintoService

class TestRecinto(unittest.TestCase):
    def setUp(self):
        self.recinto_service = RecintoService()
        self.recinto_service.criar_recinto("Savana", "Leão", "Bem cuidado")

    def test_adicionar_animal(self):
        animal = Animal("Alex", "Leão", 80)
        resultado = self.recinto_service.adicionar_animal_recinto("Savana", animal)
        self.assertTrue(resultado)

    def test_alterar_estado_cuidado(self):
        self.recinto_service.alterar_estado_recinto("Savana", "Mal cuidado")
        recintos = self.recinto_service.listar_recintos()
        self.assertEqual(recintos[0].estado_cuidado, "Mal cuidado")

if __name__ == '__main__':
    unittest.main()
