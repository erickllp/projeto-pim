class Nodo:
    def __init__(self, valor, tipo):
        self.valor = valor #Nome do paciente, descrição do impacto ou plano
        self.tipo = tipo # paciente, impacto, plano
        self.filhos = []# Lista de filhos (impactos ou planos)

    def adicionar_filho(self, nodo):
        self.filhos.append(nodo)
