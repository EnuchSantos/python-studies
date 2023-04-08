# Jogo da advinhação
palavra = 'carro'

tentativa = input('Tente descobrir se a letra existe na palavra\n digite uma letra: ')

if tentativa in palavra:
    print(f'{tentativa} existe!')
else:
    print(f'{tentativa} não existe!')
