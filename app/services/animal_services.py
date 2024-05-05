from models.animal import Animal

class AnimalService:
    def __init__(self):
        self.animais = []

    def criar_animal(self, nome, especie, felicidade):
        novo_animal = Animal(nome, especie, felicidade)
        self.animais.append(novo_animal)
        return novo_animal

    def listar_animais(self):
        return self.animais

    def alimentar_animal(self, nome):
        animal = next((a for a in self.animais if a.nome == nome), None)
        if animal:
            animal.alimentar()
            return True
        return False
