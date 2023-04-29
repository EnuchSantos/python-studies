"""
Faça um jogo para o usuário adivinhar qual a palavra secreta.
- Você vai propor uma palabra secreta qualque e vai dar a possibelidade para 
o usuário digitar ima letra, você vai conferir se a letra digitada está na 
palavra secreta.
- Se a letra digitada estiver na palavra secreta; exiba a letra;
- Se a letra digitada não estiver na palavra secreta; exiba *.
Faça a contagem de tentativas do seu usuário.
"""

secret_word = 'carro'
secret = '*' * len(secret_word)
key = False
win = len(secret_word)
count = 0
while not key:
    attempt = input("Type a letter: ")

    if len(attempt) > 1:
        print("Type only one letter, ok")
        continue

    i = 0
    hit = False

    for letter in secret_word:
        if attempt == letter:
            win -= 1
            hit = True
            secret = f'{secret[0:i]}{letter}{secret[i+1:]}'
        elif letter == secret_word[-1] and hit == True:
            print(f'Nice! {secret}')
        elif letter == secret_word[-1] and hit == False:
            print(f'Wrong! {secret}')

        i += 1

    count += 1
    print(f"Attempts: {count}")

    if win == 0:
        print("You win!!!")
        print(f'The secret word is: {secret_word}')
        break

    exit = input('Type [E]xit or [C]ontinue: ')
    if exit.lower() == 'e':
        break
