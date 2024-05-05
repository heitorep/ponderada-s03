from models.zoologico import Zoologico

class ZoologicoService:
    def __init__(self):
        self.zoologico = Zoologico("Zoo Fantástico")

    def adicionar_recinto(self, recinto):
        self.zoologico.adicionar_recinto(recinto)

    def obter_info(self):
        return {
            "nome": self.zoologico.nome,
            "receita_total": self.zoologico.receita_total,
            "total_visitas": self.zoologico.total_visitas,
            "recintos": len(self.zoologico.recintos)
        }

    def registrar_visita_receita(self, visitas, receita):
        self.zoologico.registrar_visita(visitas)
        self.zoologico.registrar_receita(receita)
