from models.visitante import Visitante

class VisitanteService:
    def __init__(self):
        self.visitantes = []

    def criar_visitante(self, nome, idade):
        novo_visitante = Visitante(nome, idade)
        self.visitantes.append(novo_visitante)
        return novo_visitante

    def listar_visitantes(self):
        return self.visitantes

    def registrar_visita_visitante(self, nome):
        visitante = next((v for v in self.visitantes if v.nome == nome), None)
        if visitante:
            visitante.registrar_visita()
            return True
        return False

    def registrar_gasto_visitante(self, nome, quantidade):
        visitante = next((v for v in self.visitantes if v.nome == nome), None)
        if visitante and quantidade > 0:
            visitante.gastar_dinheiro(quantidade)
            return True
        return False
