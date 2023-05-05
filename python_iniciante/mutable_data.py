list_a = ['Enuch', 'Santos']
# Não está copiando, list_b aponta para o mesmo local da memória que list_a
list_b = list_a
# Copiando usando o copy
list_b = list_a.copy()

list_a[0] = 'Whatever'
print(list_a)
