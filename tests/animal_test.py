import unittest
from app.services.animal_services import AnimalService

class TestAnimal(unittest.TestCase):
    def setUp(self):
        self.animal_service = AnimalService()
        self.animal_service.criar_animal("Marty", "Zebra", 50)

    def test_alimentar(self):
        self.animal_service.alimentar_animal("Marty")
        animais = self.animal_service.listar_animais()
        self.assertEqual(animais[0].felicidade, 60)

    def test_criar_animal(self):
        animal = self.animal_service.criar_animal("Alex", "Leão", 40)
        self.assertEqual(animal.nome, "Alex")
        self.assertEqual(animal.especie, "Leão")
        self.assertEqual(animal.felicidade, 40)

if __name__ == '__main__':
    unittest.main()
