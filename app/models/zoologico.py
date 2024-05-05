class Zoologico:
    def __init__(self, nome):
        self.nome = nome
        self.recintos = []
        self.receita_total = 0
        self.total_visitas = 0

    def adicionar_recinto(self, recinto):
        self.recintos.append(recinto)

    def registrar_visita(self, quantidade_visitas):
        """Incrementa o número total de visitas ao zoológico."""
        self.total_visitas += quantidade_visitas

    def registrar_receita(self, valor):
        """Incrementa a receita total do zoológico."""
        self.receita_total += valor
