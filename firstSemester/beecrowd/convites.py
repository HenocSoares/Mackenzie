'''
Faça um programa em Python que receba o custo (valor em reais) de um espetáculo teatral e o preço do convite (valor em reais) desse espetáculo. Esse programa deve calcular e mostrar:

a) A quantidade de convites que devem ser vendidos para que, pelo menos, o custo do espetáculo seja alcançado.

b) A quantidade de convites que devem ser vendidos para que se tenha um lucro de 23%.

Observe que as quantidades calculadas devem ser um número inteiro, portanto, o resultado da quantidade de convites deve ser arredondada para cima, usando a função matemática apropriada em Python.
'''

import math

custo = float(input("Entre com o custo total: "))
convite = float(input("Informe o preço do convite unitário: "))

# A quantidade de vendas (em convites) para pelo menos alcançar o custo do espetáculo.

qtd = math.ceil(custo / convite)

# A quantidade de convites que devem ser vendidos para que se tenha um lucro de 23%.

lucro = custo * 1.23
qtd_lucro = math.ceil((custo + lucro) / convite) # Cálculo da quantidade necessária de convites.

print("Quantidade mínima para alcançar o custo: ", qtd)
print("O necessário para se obter lucro de 23%: ", qtd_lucro)
