"""
Retorno de valores das funções (return)
"""


def sum_or_plus(a, b):
    if a > 10:
        return a * b
    return a + b


sum_1 = sum_or_plus(22, 2)
sum_2 = sum_or_plus(4, 4)
print(sum_or_plus(sum_1, sum_2))

"""
args - Argumentos não nomeadors
* - *args (empacotamento e desempacotamento)
"""

x, y, *resto = 1, 2, 3, 4
print(x, y, resto)


def soma(*args):
    total = 0
    for num in args:
        total += num
    return total


numeros = 1, 2, 3, 4
result = soma(*numeros)  # desempacotando
print(result)
print(sum((1, 2, 3, 4, 5)))
