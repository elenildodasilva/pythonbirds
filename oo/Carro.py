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
>>> motor =motor()
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
>>> direcao.Direcao()
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