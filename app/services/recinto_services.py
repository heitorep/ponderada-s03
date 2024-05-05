from models.recinto import Recinto

class RecintoService:
    def __init__(self):
        self.recintos = []

    def criar_recinto(self, nome, especie, estado_cuidado):
        novo_recinto = Recinto(nome, especie, estado_cuidado)
        self.recintos.append(novo_recinto)
        return novo_recinto

    def listar_recintos(self):
        return self.recintos

    def adicionar_animal_recinto(self, nome_recinto, animal):
        recinto = next((r for r in self.recintos if r.nome == nome_recinto), None)
        if recinto:
            return recinto.adicionar_animal(animal)
        return False

    def alterar_estado_recinto(self, nome_recinto, novo_estado):
        recinto = next((r for r in self.recintos if r.nome == nome_recinto), None)
        if recinto:
            recinto.alterar_estado_cuidado(novo_estado)
            return True
        return False
