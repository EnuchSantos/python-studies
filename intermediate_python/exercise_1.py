"""
1 - Crie uma função que multiplica todos os argumentos não nomeados recebidos.
Retorne o total para uma variável e mostre o valor da variável.

2 - Cria uma função que fala se o número é par ou ímpar.
"""

# Solução 1


def plus(*nums):
    total = 1
    for num in nums:
        total *= num
    return total


result = plus(2, 2, 3, 4, 5)
print(result)


def even_or_odd(num):
    return 'Even' if num % 2 == 0 else 'ODD'


print(even_or_odd(3))
