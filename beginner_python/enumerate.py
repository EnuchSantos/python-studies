# Enumeradores

lista = ["Enuch", "Isaque", "Erika", "Lucas"]

# possivel definir um start de indice
lista_enumerada = enumerate(lista, start=10)
# convertendo um enumerate em lista
# lista_convertida = tuple(lista_enumerada)
# print(lista_convertida)

# for item in lista_enumerada:
#     indice, nome = item
#     print(item)
#     print(indice, nome)

for indice, nome in lista_enumerada:
    print(indice, nome)
