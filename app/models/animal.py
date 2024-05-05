class Animal:
    def __init__(self, nome, especie, felicidade):
        self.nome = nome
        self.especie = especie
        self.felicidade = felicidade

    def alimentar(self):
        """Aumenta a felicidade do animal em 10 pontos."""
        self.felicidade += 10
