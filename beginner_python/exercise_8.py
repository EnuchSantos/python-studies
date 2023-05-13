nome = 'Enuch Santos'
count = 0
new_string = '*'

while count < len(nome):
    new_string += f'{nome[count]}*'
    count += 1

print(new_string)
