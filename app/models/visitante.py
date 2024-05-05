class Visitante:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.visitas = 0
        self.dinheiro_gasto = 0

    def registrar_visita(self):
        """Registra uma nova visita do visitante ao zoológico."""
        self.visitas += 1

    def gastar_dinheiro(self, quantidade):
        """Acumula o total de dinheiro gasto pelo visitante no zoológico."""
        self.dinheiro_gasto += quantidade
