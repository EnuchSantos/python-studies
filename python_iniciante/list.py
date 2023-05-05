"""
Listas em python
Listas mutaveis
Heterogemeas 
- metedos: append, insert, pop, del, clear, extend
"""

# lista = list()
# lista = [1, 2, 3, 4]
# print(lista)
# del lista[1]  # deleta o item pelo indice
# print(lista)
# lista.append(5)
# lista.append(6)
# print(lista)
# valor_removido = lista.pop()  # remove o ultimo valor da lista e retorna
# print(lista)
# lista.insert(0, 79)  # inseri em qualquer lugar da lista
# print(lista)

list_a = [1, 2, 3]
list_b = [4, 5, 6]
list_c = list_a + list_b
list_c.extend([7, 8, 9])
print(list_c)
