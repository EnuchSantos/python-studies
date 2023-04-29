sexo = 'sexo'
new_string = ''
for letter in sexo:
    new_string += f'*{letter}'
    print(letter)

print(new_string + '*')

# for continue break

for i in range(10):
    if i == 2:
        print("i é 2, pulando...")
        continue

    if i == 8:
        print('i é 8, seu else não executará')
        break

    for j in range(1, 3):
        print(i, j)
else:
    print('For completo com sucesso')
