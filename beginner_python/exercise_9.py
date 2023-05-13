phrase = 'O python é uma linguagem de programação ' \
    'multiparadigma. ' \
    'Python foi criado por Guido Van Rossum.'

i = 0
j = 0
number = 0
greater_number = 0
greater_letter = ''
while i < len(phrase):
    actually_letter = phrase[i]

    while j < len(phrase):
        if actually_letter == phrase[j]:
            number += 1
        j += 1

    if number > greater_number:
        greater_number = number
        greater_letter = actually_letter

    i += 1
    j = 0
    number = 0

print(
    f'A letra que apareceu mais vezes foi a: {greater_letter} sendo {greater_number}x')


# outra forma com count
qtd_apareceu_mais = 0
letra_apareceu_mais = ''
while i < len(phrase):
    letra_atual = phrase[i]
    qtd_apareceu_mais_atual = phrase.count(letra_atual)

    if qtd_apareceu_mais < qtd_apareceu_mais_atual:
        qtd_apareceu_mais = qtd_apareceu_mais_atual
        letra_apareceu_mais = letra_atual

    i += 1

print(
    f'A letra que apareceu mais vezes foi a: {letra_apareceu_mais} sendo {qtd_apareceu_mais}x')
