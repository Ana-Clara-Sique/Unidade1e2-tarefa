class Problema:
    def __init__(self, numero_macas_inicial, numero_macas_dadas):
        self.numero_macas_inicial = numero_macas_inicial
        self.numero_macas_dadas = numero_macas_dadas

    def calcular_macas_restantes(self):
        return self.numero_macas_inicial - self.numero_macas_dadas    