string = 'valorqualquer'
i = 0

while i < len(string):
    letra = string[i]

    if letra == ' ':
        break

    print(letra)
    i += 1
else:
    print('Não foi encontrado espaço na string')

print('Fora do while')
