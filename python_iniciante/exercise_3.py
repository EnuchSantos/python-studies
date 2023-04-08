# Sisteminha de senha com operadores lógicos

entrar = input('[E] para entrar ou [S] para sair')
senha = input('Digite sua senha: ')

senha_usuario = '12345'

if (entrar == 'E' or 'e') and senha_usuario == senha:
    print("Bem vindo ao Enuch's")
else:
    print('Saiu')