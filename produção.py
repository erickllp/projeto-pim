import random

class Producao:
    def __init__(self, materiaPrima=2):
        self.materiaPrima = materiaPrima
        self.historico_falhas = []

    def calcular_materia_prima(self, qtd_pacientes):
        return qtd_pacientes * self.materiaPrima

    def falhaAmbiental(self, qtd_pacientes):
        if qtd_pacientes > 50:
            falha = "ALTO risco de falha ambiental"
        elif qtd_pacientes >= 20:
            falha = "MÉDIO risco de falha ambiental"
        else:
            falha = "BAIXO risco de falha ambiental"

        ocorreu = random.choice([True, False])
        self.historico_falhas.append((qtd_pacientes, falha, ocorreu))
        return falha, ocorreu

    def consultar_historico(self):
        if not self.historico_falhas:
            print("Nenhuma falha registrada ainda.")
        else:
            for i, (pacientes, risco, ocorreu) in enumerate(self.historico_falhas, start=1):
                print(f"{i}. Pacientes: {pacientes}, Risco: {risco}, Falha ocorreu? {'Sim' if ocorreu else 'Não'}")
