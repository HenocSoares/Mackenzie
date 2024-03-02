'''
Faça um programa em Python que recebe o custo (valor em reais)
de um espetáculo teatral e o preço do convite (valor em reais)
desse espetáculo. Esse programa deve calcular e mostrar:

a) A quantidade de convites que devem ser vendidos para que,
pelo menos, o custo do espetáculo seja realizado.
b) A quantidade de convites que deverão ser vendidos para que
você tenha um lucro de 23%.

Observe que as peças calculadas devem ser um número inteiro, 
portanto, o resultado da quantidade de convites deve ser 
arredondado para cima, usando a função matemática detalhada em Python.
'''

import math

custo = float(input("Informe o custo total do espetáculo (R$): "))
preco_do_convite = float(input("Agora o preço (R$) do convite: "))

qtd_min_a_vender = math.ceil(custo / preco_do_convite)
