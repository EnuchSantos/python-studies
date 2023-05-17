"""
Higher Order Functions
Funções de primeira classe
"""


def saudacao(msg, nome):
    return f'{msg} {nome}'


def executa(function, *text):
    return function(*text)


saudacao_2 = saudacao
v = executa(saudacao_2, 'Faça sexo', 'Enuch')
print(v)
