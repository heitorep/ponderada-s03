class Recinto:
    def __init__(self, nome, especie, estado_cuidado):
        self.nome = nome
        self.especie = especie
        self.estado_cuidado = estado_cuidado
        self.animais = []

    def adicionar_animal(self, animal):
        if animal.especie == self.especie:
            self.animais.append(animal)
            return True
        return False

    def alterar_estado_cuidado(self, novo_estado):
        self.estado_cuidado = novo_estado
