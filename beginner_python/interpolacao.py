# Interpolação básica de strings

# s - string
# d e i - int
# f - float
# x e X - hexadecimal

nome = 'Enuch'
preco = 100.12313
variavel = '%s, o preço é R$%f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %04X' % (1500, 1500)) #pode ser %08X