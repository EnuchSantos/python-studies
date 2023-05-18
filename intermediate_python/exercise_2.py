"""
Crie funções que duplical, triplicam e quadruplicam o número recebido
"""


def create_multiplier(multiplier):
    def multiply(num):
        return num * multiplier
    return multiply


duplicar = create_multiplier(2)
print(duplicar(10))
