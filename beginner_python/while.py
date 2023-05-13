# count = 0
# while count < 10:
#     print('faça sexo amigo')
#     count += 1

# senha = '1234'
# passe = False

# while not passe:
#     senha_test = input("digite sua senha: ")
#     if senha_test == senha:
#         passe = True

# while True:
#     yes_or_not = input("Do you wanna be my girlfriend? 1 - yes 2 - not\n")

#     if yes_or_not == '1':
#         print('I love you')
#     elif yes_or_not == '2':
#         print('Fuck you, your fucking bitch')
#     else:
#         break


# count = 0

# while count <= 20:
#     count += 1
#     if count % 2 == 0:
#         continue

#     print(f"All numbers odd {count}")


linha = 1
qtd_linha = 5

coluna = 1

while linha <= qtd_linha:
    while coluna <= qtd_linha * linha:
        print(f'{linha=} {coluna=}')
        coluna += 1

    linha += 1
