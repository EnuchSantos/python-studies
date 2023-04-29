"""
Listas em python
Listas mutaveis
Heterogemeas 
- metedos: append, insert, pop, del, clear, extend
"""

lista = list()
lista = [1, 2, 3, 4]
print(lista)
del lista[1]  # deleta o item pelo indice
print(lista)
lista.append(5)
lista.append(6)
print(lista)
valor_removido = lista.pop()
print(lista)
