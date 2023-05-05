# Desempacotamento e empacotamento
names = ['Enuch', 'Santos', 'Araujo']

name1, name2, name3 = names
print(name1)

# pegando apenas um valor e liberando o resto em uma variavel
# Usar '_' como convenção
age, *_ = [24, 20, 30]
print(age, _)
_, age, *_ = [24, 20, 30]
print(age, _)

# tuple
tupla = ('Olá', 'Sexo', 'Carro')
print(tupla)
