"""
Introdução às funções em python (def)
Funções são trechos de código usados para replicar determinada ação
ao longo do seu código.
Elas podem receber valores parâmetros (argumentos) e retornar um valor específico.
Por padrão def retornam none (nada)
"""


def Print(text: str, times: int):
    return print(text * times)


Print('Enuch ', 2)
