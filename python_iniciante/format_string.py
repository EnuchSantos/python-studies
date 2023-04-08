a = 'a'
b = 'b'
c = 'c'

# simples
string = 'a={}'.format(a)
# indice e argumentos
string_2 = 'a={1} b={0} c={2}'.format(a, b, c)
# parametro nomeado
string_3 = 'a={1} b={0} c={parametro3}'.format(a, b, parametro3=c)

print(string)
print(string_2)
print(string_3)