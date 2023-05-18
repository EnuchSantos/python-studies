"""
Closure e funções que retornam outras funções
"""


def create_saudation(saudation):
    def salut(name):
        return f'{saudation}, {name}'
    return salut


var = create_saudation('Bom dia')
print(var('Enuch'))
