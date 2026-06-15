import time

class Jogador:

    def __init__(self):

        self.acertos = 0
        self.erros = 0

        self.pontos = {
            "matematica": 0,
            "logica": 0,
            "sequencia": 0
        }

        self.nivel = {
            "matematica": 1,
            "logica": 1,
            "sequencia": 1
        }

        self.tempo_inicio = 0

    def iniciar_tempo(self):
        self.tempo_inicio = time.time()

    def calcular_bonus_tempo(self):

        tempo = time.time() - self.tempo_inicio

        if tempo < 10:
            return 5
        elif tempo < 20:
            return 3
        elif tempo < 30:
            return 1
        else:
            return 0

    def atualizar_nivel(self, categoria):

        pontos = self.pontos[categoria]
        nivel_anterior = self.nivel[categoria]

        if pontos < 30:
            self.nivel[categoria] = 1

        elif pontos < 70:
            self.nivel[categoria] = 2

        elif pontos < 120:
            self.nivel[categoria] = 3

        else:
            self.nivel[categoria] = 4

        # feedback simples (opcional)
        if self.nivel[categoria] > nivel_anterior:
            print(f"↑ Subiu nível em {categoria}!")

    def acertou(self, categoria):

        self.acertos += 1

        bonus = self.calcular_bonus_tempo()

        self.pontos[categoria] += 10 + bonus

        # bônus leve por desempenho alto
        if self.pontos[categoria] > 40:
            self.pontos[categoria] += 2

        self.atualizar_nivel(categoria)

    def errou(self, categoria):

        self.erros += 1

        self.pontos[categoria] -= 7

        if self.pontos[categoria] < 0:
            self.pontos[categoria] = 0

        self.atualizar_nivel(categoria)