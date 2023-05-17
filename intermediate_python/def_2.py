"""_summary_
Retorno de valores das funções (return)
"""


def sum_or_plus(a, b):
    if a > 10:
        return a * b
    return a + b


sum_1 = sum_or_plus(22, 2)
sum_2 = sum_or_plus(4, 4)
print(sum_or_plus(sum_1, sum_2))
