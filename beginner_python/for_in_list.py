list_a = ["Enuch", "Erika", "Effy"]

i = 0
for nome in list_a:
    print(nome, i, type(nome))
    i += 1

# another way
index = range(len(list_a))
for i in index:
    print(i, list_a[i], type(list_a[i]))
