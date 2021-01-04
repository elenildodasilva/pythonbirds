

"""
voce deve criar uma classe carro que vai possuir 2 atributos compostos por outras duas classes:
motor
direção
o motor terá a responsabilidade de controlar a velocidade
ele oferece os seguintes atributtos:
1) Atributo de dado - Velocidade
2) método acelerar, que deverá  incrementar  a velociade de uma unidade
3) método frear que deverá decrementar a velocidade em duas unidades

A Direção terá a responsabilidade de controlar a direção. Ela oferece os seguintes atributos:
1) Valor da direção com valores possiveis: Norte, sul, leste, oeste
2) método girar a direita: deverá girar a direção para a direita
3) método girar a esquerda: deverá girar a direção para a esquerda

   N
O     L
   S

Exemplo:
>>> # Testando motor
>>> motor = Motor()
>>> motor.velocidade
0
>>> motor.acelerar()
>>> motor.velocidade
1
>>> motor.acelerar()
>>> motor.velocidade
2
>>> motor.acelerar()
>>> motor.velocidade
3
>>> motor.frear()
>>> motor.velocidade
1
>>> motor.frear()
>>> motor.velocidade
0
>>> # Testando direcao
>>> direcao = Direcao()
>>> direcao.valor
'Norte'
>>> direcao.girar_a_direita()
>>> direcao.valor
'Leste'
>>> direcao.girar_a_direita()
>>> direcao.valor
'Sul'
>>> direcao.girar_a_direita()
>>> direcao.valor
'Oeste'
>>> direcao.girar_a_direita()
>>> direcao.valor
'Norte'
>>> direcao.girar_a_esquerda()
>>> direcao.valor
'Oeste'
>>> direcao.girar_a_esquerda()
>>> direcao.valor
'Sul'
>>> direcao.girar_a_esquerda()
>>> direcao.valor
'Leste'
>>> direcao.girar_a_esquerda()
>>> direcao.valor
'Norte'
>>> carro = Carro(direcao, motor)
>>> carro.calcular_velocidade()
0
>>> carro.calcular_acelerar()
>>> carro.calcular_velocidade()
1
>>> carro.calcular_acelerar()
>>> carro.calcular_velocidade()
2
>>> carro.calcular_frear()
>>> carro.calcular_velocidade()
0

>>> carro.calcular_direcao()
>>> 'Norte'
>>> carro.girar_a_direita()
>>> carro.calcular_direcao()
>>> 'Leste'

>>> carro.girar_a_esquerda()
>>> carro.calcular_a_direcao()
>>> 'Norte'

>>> carro.girar_a_esquerda()
>>> carro.calcular_a_direcao()
>>> 'Oeste'
"""
class Motor:
    def __init__(self):
        self.velocidade=0
    def acelerar(self):
        self.velocidade+=1
    def frear(self):
        self.velocidade-=2
        self.velocidade=max(0, self.velocidade)

NORTE ='Norte'
SUL   ='Sul'
LESTE ='Leste'
OESTE ='Oeste'

class Direcao:
    rotacao_a_direita_dct = {NORTE: LESTE, LESTE: SUL, SUL: OESTE, OESTE: NORTE}
    rotacao_a_esquerda_dct = {NORTE: OESTE, OESTE: SUL, SUL: LESTE, LESTE: NORTE}

    def __init__(self):
        self.valor = NORTE
    def girar_a_direita(self):
        self.valor = self.rotacao_a_direita_dct[self.valor]
    def girar_a_esquerda(self):
        self.valor = self.rotacao_a_esquerda_dct[self.valor]


"""

ou

        if self.valor == NORTE:
           self.valor = LESTE
        elif self.valor == LESTE:
            self.valor = SUL
        elif self.valor == SUL:
            self.valor = OESTE
        elif self.valor == SUL:
            self.valor = OESTE
        elif self.valor == OESTE:
            self.valor = NORTE
"""